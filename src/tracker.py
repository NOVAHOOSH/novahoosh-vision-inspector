"""
Object Tracking Module

Maintains object identity between frames.
"""


class Tracker:


    def __init__(self):

        print("Tracker initialized")


    def update(self, detections):

        tracks = detections

        return tracks