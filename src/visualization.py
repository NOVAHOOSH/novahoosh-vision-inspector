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
        self.recording = config["recording"]
        self.fps = config["fps"]
        self.display = config["display"]
        self.writer = None
        self.running=True

    def run(self):
        print("Visualization Started")
        last_time = time.time()
        while self.running:
            if not self.frame_queue.empty():
                packet_in=self.frame_queue.get_nowait()
                frame_out = self.drawer(packet_in,last_time)
                self.recorder(frame_out)
                if self.display:
                    cv2.imshow( "NOVAHOOSH Vision Inspector        \t      Press & Hold (q) on Keyboard for exit",frame_out)
                last_time = time.time()

                if (cv2.waitKey(1) & 0xFF == ord('q')):
                    print("Request STOP")
                    self.running=False
                    self.stop_queue.put_nowait(True)
                    break
            else:
                time.sleep(0.0001)
                    
        if self.display:
            cv2.destroyAllWindows()

        if self.writer is not None:
            self.writer.release()
            self.writer = None

        print("Visualization Stopped")

    def recorder(self,frame):
        if self.recording and self.writer is None:
            height, width = frame.shape[:2]
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            self.writer = cv2.VideoWriter(self.output,fourcc,self.fps,(width, height))

            if not self.writer.isOpened():
                print("ERROR: Cannot open output video")
                self.writer = None
        if self.recording and self.writer is not None:
            self.writer.write(frame)

    def drawer(self,packet_in,last_time):
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
                delta_t = (time.time()-last_time) 
                if delta_t==0:
                    fps = 100
                else: 
                    fps = int(10/delta_t)/10
                cv2.putText(frame,"FPS : "+str(fps),(weight-100,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
        return frame

    def stop(self):
        self.running=False