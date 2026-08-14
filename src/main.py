from queue import Queue
from config import CONFIG
from getframe import GetFrame
from visualization import Visualization



def main():
    frame_queue = Queue(maxsize=CONFIG["queue_size"])
    STOP = Queue(maxsize=1)
    grabber = GetFrame(frame_queue,CONFIG,STOP)
    viewer = Visualization(frame_queue,CONFIG,STOP)

    grabber.start()
    viewer.start()

    viewer.join()
    grabber.join()



if __name__=="__main__":
    main()