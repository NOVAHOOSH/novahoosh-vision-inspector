from queue import LifoQueue
from config import CONFIG
from getframe import GetFrame
from visualization import Visualization
from detector import Detector

import warnings
warnings.filterwarnings("ignore",message="torch.meshgrid: in an upcoming release")



def main():
    frame_queue = LifoQueue(maxsize=1)
    STOP = LifoQueue(maxsize=1)
    detector_queue = LifoQueue(maxsize=1)
    grabber = GetFrame(frame_queue,CONFIG,STOP)
    detector = Detector(frame_queue,detector_queue,CONFIG,STOP)
    viewer = Visualization(detector_queue,CONFIG,STOP)

    grabber.start()
    detector.start()
    viewer.start()

    viewer.join()
    detector.join()
    grabber.join()


if __name__=="__main__":
    main()