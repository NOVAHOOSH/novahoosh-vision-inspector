import cv2
from threading import Thread
import time

class GetFrame(Thread):
    def __init__(self, frame_queue, config, stop):
        super().__init__()
        self.frame_queue = frame_queue
        self.stop = stop
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
        exit = False
        while self.running:
            ret, frame = cap.read()
            if not ret:
                print("Reloaded Video")
                #cap.release()
                cap = cv2.VideoCapture(self.source)#,cv2.CAP_FFMPEG, [cv2.CAP_PROP_HW_ACCELERATION, cv2.VIDEO_ACCELERATION_ANY ])
                _, frame = cap.read()

            if self.frame_queue.empty():
                self.frame_queue.put_nowait(frame)
                t_now = time.time()
                if (t_now-t_last) < (1/self.fps) :
                    time.sleep(1/self.fps - t_now + t_last)
                t_last = t_now

            else:
                try:
                    _ = self.frame_queue.get_nowait()
                    self.frame_queue.put_nowait(frame)
                    cv2.waitKey(1)
                except:
                    continue

            if (not self.stop.empty()):
                exit = self.stop.get_nowait()
                self.stop.put_nowait(exit)

            if exit:
                self.running=False
                break
            
        cap.release()
        print("Frame Grabber Stopped")

    def stop(self):
        self.running=False