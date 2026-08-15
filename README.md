# NOVAHOOSH Vision Inspector

> AI-powered computer vision pipeline for industrial production-line inspection.

![Status](https://img.shields.io/badge/status-active%20development-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![License](https://img.shields.io/badge/license-MIT-blue)

🚧 **Status: Active Development / Prototype**

NOVAHOOSH Vision Inspector is a computer vision prototype designed to
demonstrate AI-based visual inspection for industrial production-line
environments.

The project focuses on detecting and analyzing products moving through
a production process using camera-based computer vision.

---

## Overview

Industrial production lines often require continuous visual inspection
to identify defective products, monitor production processes, and maintain
consistent quality.

Manual inspection can be:

- Time-consuming
- Expensive
- Inconsistent
- Difficult to scale
- Dependent on human attention

NOVAHOOSH Vision Inspector explores an AI-based approach in which
production-line video is processed automatically to detect and analyze
products.

The initial demonstration focuses on a beverage-production scenario,
with particular attention to visual inspection of bottle caps.

The architecture is intended to be adaptable to other industrial
inspection applications.

---

## Demo

### Object Detection

The current prototype processes industrial production-line footage
and performs AI-based object detection.

![Object Detection Demo](results/Detection/detection_demo.gif)

The GIF above is a short demonstration of the current development state.

A complete demonstration video and additional results will be added
as the project progresses.

---

## Current Capabilities

### Implemented

- [x] Video input
- [x] Object detection
- [x] Visualization of detection results

### In Development

- [ ] Multi-object tracking
- [ ] Production-line object counting
- [ ] Defect classification
- [ ] Inspection decision logic
- [ ] Performance evaluation
- [ ] Industrial deployment pipeline

The project is intentionally being developed incrementally.
Production deployment is not currently claimed.

---

# Industrial Use Case

## Bottle Cap Inspection

The initial use case demonstrates how computer vision can be applied
to inspect bottle caps in a beverage production environment.

A production-line inspection system could potentially identify
conditions such as:

- Missing caps
- Incorrect cap placement
- Damaged caps
- Abnormal product appearance
- Other visually detectable production defects

The current repository represents a prototype demonstrating the
underlying computer vision pipeline rather than a production-certified
inspection system.

---

# System Pipeline

The planned inspection pipeline follows the structure:

```text
Production-Line Camera / Video
            │
            ▼
      Video Acquisition
            │
            ▼
      Object Detection
            │
            ▼
      Object Tracking
            │
            ▼
     Defect / Quality Analysis
            │
            ▼
      Inspection Decision
            │
            ▼
       Quality Output