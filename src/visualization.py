import time
import cv2
from threading import Thread

class_name = {39:"bottle",1:"cap"}
class Visualization(Thread):
    def __init__(self, frame_queue, config, stop_queue):
        super().__init__()
        self.frame_queue = frame_queue
        self.output = config["output"]
        self.stop_queue = stop_queue
        self.running=True

    def run(self):
        print("Visualization Started")
        while self.running:
            if not self.frame_queue.empty():
                packet_in=self.frame_queue.get_nowait()
                frame_out = self.drawer(packet_in)
                cv2.imshow( "NOVAHOOSH Vision Inspector        \t      Press & Hold (q) on Keyboard for exit",frame_out)

                if (cv2.waitKey(1) & 0xFF == ord('q')):
                    print("Request STOP")
                    self.running=False
                    self.stop_queue.put_nowait(True)
                    break
            else:
                time.sleep(0.0001)

        cv2.destroyAllWindows()
        print("Visualization Stopped")

    def drawer(self,packet_in):
        frame = packet_in["frame"]
        if packet_in["detections"]:
            height,weight,_ = frame.shape
            for det in packet_in["detections"]:
                #cx,cy,w,h,class_id,conf_id=det
                x1,y1,x2,y2,class_id,conf_id=det
                #x1,y1,x2,y2=int(min(max(cx-w/2,0),weight)),int(min(max(cy-h/2,0),height)),int(min(max(cx+w/2,0),weight)),int(min(max(cy+h/2,0),height))
                #print(x1,y1,x2,y2,class_id,conf_id)
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(frame,(x1,y1-30),(x2,y1),(0,255,0),-1)
                cv2.putText(frame,class_name[class_id]+"-"+str(conf_id),(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
        return frame

    def stop(self):
        self.running=False