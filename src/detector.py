import time
import sys
import time
import contextlib
import io
import cv2
import torch
from threading import Thread

# Add YOLOv7 path
sys.path.append("third_party/yolov7")

from models.experimental import attempt_load
from utils.general import (non_max_suppression,scale_coords)
from utils.torch_utils import (select_device)
from utils.datasets import letterbox
from utils.general import scale_coords

class Detector(Thread):
    def __init__(self, frame_queue, detection_queue, config, stop_queue):
        super().__init__()
        self.frame_queue = frame_queue
        self.detection_queue = detection_queue
        self.stop_queue = stop_queue
        self.running = True
        self.weights = config["weights"]
        self.device_name = config["device"]
        self.img_size = config["img_size"]
        self.confidence = config["confidence"]
        self.load_model()

    def load_model(self):
        print("Loading YOLOv7 model...")
        self.device = select_device(self.device_name)
        with contextlib.redirect_stdout(io.StringIO()):
            self.model = attempt_load(self.weights,map_location=self.device)
        
        self.model.eval()
        print("YOLOv7 loaded")

    def run(self):
        print("Detector Started")
        exit_flag = False
        result_detection = []
        while self.running:
            if not self.frame_queue.empty():
                packet_in = self.frame_queue.get_nowait()
                result_detection = self.inference(packet_in["frame"])

                packet_out = {"frame": packet_in["frame"],
                              "detections": result_detection,
                              "time": time.time()}

                # Update Detection
                if not self.detection_queue.empty():
                    _ = self.detection_queue.get()
                self.detection_queue.put_nowait(packet_out)
            else:
                time.sleep(0.0001)

            # Stop check
            if (not self.stop_queue.empty()):
                exit_flag = self.stop_queue.get_nowait()
                self.stop_queue.put_nowait(exit_flag)

            if exit_flag:
                self.running=False
                break

        print("Detector Stopped")

    def inference(self, frame):
        """
        YOLOv7 inference
        """
        img = self.preprocess(frame)
        with torch.no_grad():
            pred = self.model(img)[0]

        pred = non_max_suppression(pred,self.confidence)

        results=[]
        for det in pred:
            if len(det):
                det[:, :4] = scale_coords(img.shape[2:],det[:, :4],frame.shape).round()
                for *xyxy, conf, class_id in det:
                    if int(class_id.cpu().numpy()) == 39: # bottle
                        results.append([int(xyxy[0]),int(xyxy[1]),
                                        int(xyxy[2]),int(xyxy[3]),
                                        int(class_id.cpu().numpy()),
                                        int(conf.cpu().numpy()*1000)/10])

        return results

    #def preprocess(self, frame):
    #    img = frame.copy()
    #    # BGR -> RGB
    #    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #    # HWC -> CHW
    #    img = img.transpose(2, 0, 1)
    #    # numpy -> tensor
    #    img = torch.from_numpy(img)
    #    # add batch dimension
    #    img = img.unsqueeze(0)
    #    img = img.to(self.device)
    #    img = img.float()
    #    img /= 255.0

    #    return img

    def preprocess(self, frame):

        img = letterbox(frame, self.img_size,stride=32,auto=True)[0]
        img = img[:, :, ::-1].transpose(2,0,1)
        img = img.copy()
        img = torch.from_numpy(img)
        img = img.to(self.device)
        img = img.float()
        img /= 255.0
        if img.ndimension()==3:
            img = img.unsqueeze(0)

        return img

    def stop_thread(self):

        self.running=False