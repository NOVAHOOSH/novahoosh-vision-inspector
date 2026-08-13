"""
NOVAHOOSH Vision Inspector

Main application pipeline

Camera / Video
      |
Detector
      |
Tracker
      |
Defect Classifier
      |
Visualization
"""


from detector import Detector
from tracker import Tracker
from defect_classifier import DefectClassifier
from visualization import Visualizer


def main():

    print("NOVAHOOSH Vision Inspector Started")

    detector = Detector()
    tracker = Tracker()
    classifier = DefectClassifier()
    visualizer = Visualizer()

    print("AI pipeline initialized")


if __name__ == "__main__":
    main()