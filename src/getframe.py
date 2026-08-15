import cv2
from threading import Thread
import time

class GetFrame(Thread):
    def __init__(self, frame_queue, config, stop_queue):
        super().__init__()
        self.frame_queue = frame_queue
        self.stop_queue = stop_queue
        self.source = config["source"]
        self.fps = config["fps"]
        self.running = True

    def run(self):
        print("Frame Grabber Started")
        cap = cv2.VideoCapture(self.source)#,cv2.CAP_FFMPEG, [cv2.CAP_PROP_HW_ACCELERATION, cv2.VIDEO_ACCELERATION_ANY ])
        if not cap.isOpened():
            print("ERROR: Cannot open video source / Check Address!")
            self.running = False
            return

        t_last = time.time()
        exit_flag = False
        while self.running:
            ret, frame = cap.read()
            if not ret:
                print("Reloaded Video")
                #cap.release()
                cap = cv2.VideoCapture(self.source)#,cv2.CAP_FFMPEG, [cv2.CAP_PROP_HW_ACCELERATION, cv2.VIDEO_ACCELERATION_ANY ])
                _, frame = cap.read()

            packet_out = {"frame": frame,
                            "detections": [],
                            "time": time.time()}

            if self.frame_queue.empty():
                self.frame_queue.put_nowait(packet_out)
                t_now = time.time()
                if (t_now-t_last) < (1/self.fps) :
                    time.sleep(1/self.fps - t_now + t_last)
                t_last = time.time()

            else:
                self.frame_queue.get()
                self.frame_queue.put_nowait(packet_out)
                cv2.waitKey(1)

            if (not self.stop_queue.empty()):
                exit_flag = self.stop_queue.get_nowait()
                self.stop_queue.put_nowait(exit_flag)

            if exit_flag:
                self.running=False
                break
            
        cap.release()
        print("Frame Grabber Stopped")

    def stop(self):
        self.running=False