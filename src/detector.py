import time
import cv2
from threading import Thread

class Detector(Thread):

    def __init__(self, frame_queue, detection_queue, stop_queue):
        super().__init__()
        self.frame_queue = frame_queue
        self.detection_queue = detection_queue
        self.stop_queue = stop_queue
        self.running = True

    def run(self):
        print("Detector Started")
        exit_flag = False
        while self.running:
            if not self.frame_queue.empty():
                packet_in = self.frame_queue.get_nowait()
                result_detection = self.process(packet_in["frame"])

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

    def process(self, frame):
        """
        Temporary detector
        Replace with YOLOv7 later
        """
        h,w,_ = frame.shape
        #print(h,w)

        # Fake detection
        detection = [int(w*0.3),int(h*0.3),int(w*0.3),int(h*0.3),0,0.95]
        return [detection]

    def stop_thread(self):

        self.running=False