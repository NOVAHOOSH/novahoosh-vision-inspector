import cv2
from threading import Thread


class Visualization(Thread):
    def __init__(self, frame_queue, config, stop):
        super().__init__()
        self.frame_queue = frame_queue
        self.output = config["output"]
        self.stop = stop
        self.running=True

    def run(self):
        print("Visualization Started")
        while self.running:
            if not self.frame_queue.empty():
                try:
                    frame=self.frame_queue.get_nowait()
                    cv2.imshow( "NOVAHOOSH Vision Inspector        \t      Press (q) for exit",frame)
                    cv2.waitKey(1)
                except:
                    continue

                if (cv2.waitKey(1) & 0xFF == ord('q')):
                    self.running=False
                    self.stop.put_nowait(True)

        cv2.destroyAllWindows()
        print("Visualization Stopped")

    def stop(self):
        self.running=False