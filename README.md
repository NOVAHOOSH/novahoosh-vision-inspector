# NOVAHOOSH Vision Inspector

> AI-powered computer vision pipeline for industrial production-line inspection.

![Status](https://img.shields.io/badge/status-active%20development-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![License](https://img.shields.io/badge/license-MIT-blue)

**NOVAHOOSH Vision Inspector** is an AI-powered computer vision prototype developed by **NOVAHOOSH** for automated visual inspection in high-speed production environments.

The initial demonstration focuses on **beverage bottle-cap inspection**, where incorrect or defective cap installation can lead to liquid leakage, product waste, packaging damage, additional cleaning costs, and reduced product quality.

The project demonstrates how artificial intelligence, computer vision, object detection, tracking, and real-time processing can be combined into an industrial inspection pipeline.

---
🎥 Demo

![Object Detection Demo](results/Detection/detection_demo.gif)
---
> 🚧 **Project Status: Prototype / Demonstration**


# 🎯 Industrial Problem

In beverage manufacturing, correct bottle-cap installation is critical for product quality and packaging reliability.

A defective cap may cause:

- Liquid leakage
- Damaged transportation boxes
- Product waste
- Cleaning and maintenance costs
- Reduced production efficiency
- Customer dissatisfaction
- Damage to brand reputation

Traditional manual inspection becomes increasingly difficult as production speed increases.

The objective of this project is to demonstrate an automated vision-based inspection system capable of continuously analyzing products without adding a manual inspection step to the production line.

---

# 💡 NOVAHOOSH Approach

NOVAHOOSH Vision Inspector separates the inspection process into independent processing stages.

```
                    Input
                      │
                      ▼
               ┌─────────────┐
               │  GetFrame   │
               │    Thread   │
               └──────┬──────┘
                      │
                      ▼
               ┌─────────────┐
               │   Detector  │
               │    Thread   │
               └──────┬──────┘
                      │
                      ▼
               ┌─────────────┐
               │   Tracker   │
               │    Thread   │
               └──────┬──────┘
                      │
                      ▼
               ┌─────────────┐
               │Visualization│
               │    Thread   │
               └──────┬──────┘
                      │
                      ▼
                Inspection
                  Output
```
Each processing stage operates independently and communicates with the next stage through bounded queues.
This architecture allows individual processing components to be developed, tested, optimized, and replaced independently.
________________________________________
🚀 Current Demo
```
The current prototype demonstrates:
•	Video-based frame acquisition
•	Real-time AI object detection
•	CUDA-based inference
•	Configurable detection confidence
•	Multi-threaded processing
•	Detection visualization
•	Processed-video recording
•	YOLOv7 integration as an independent detection backend
•	SORT-based tracking architecture
•	Configurable runtime parameters
```
The current implementation is intentionally focused on demonstrating the core technical pipeline.
The architecture is designed to evolve toward a complete industrial inspection system.
________________________________________
🔍 Detection Pipeline

The current detection pipeline uses YOLOv7 as the object-detection backend.
YOLOv7 is treated as one component of the inspection system rather than the complete NOVAHOOSH solution.
```
Input Frame
     │
     ▼
Pre-processing
     │
     ▼
YOLOv7 Inference
     │
     ▼
Non-Maximum Suppression
     │
     ▼
Coordinate Transformation
     │
     ▼
Detection Results
     │
     ▼
Tracking
     │
     ▼
Visualization
```
The NOVAHOOSH application controls the surrounding pipeline, configuration, frame flow, visualization, recording, and future inspection logic.
________________________________________
🧵 Multi-Threaded Architecture

The prototype uses independent processing threads.
```
GetFrame
   │
   ▼
 Queue
   │
   ▼
Detector
   │
   ▼
 Queue
   │
   ▼
Tracker
   │
   ▼
 Queue
   │
   ▼
Visualization
```
A small queue size can be used to prioritize recent frames and avoid excessive processing latency.
This design is particularly useful for real-time production-line applications where processing the newest available frame may be more important than processing every historical frame.
________________________________________
📁 Project Structure
```
novahoosh-vision-inspector
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── config.py
│   ├── getframe.py
│   ├── detector.py
│   ├── tracker.py
│   ├── defect_classifier.py
│   ├── visualization.py
│   └── main.py
│
├── third_party/
│   ├── yolov7/
│   └── sort/
│
├── weights/
│   └── README.md
│
├── demo/
│   ├── input_video.mp4
│   └── result_video.mp4
│
├── docs/
│   ├── architecture.md
│   └── industrial_application.md
│
└── results/
    └── metrics.md
```
________________________________________
⚙️ Installation

1. Clone the Repository

Clone the NOVAHOOSH Vision Inspector repository:
```
git clone https://github.com/NOVAHOOSH/novahoosh-vision-inspector.git
```
Enter the project directory:
```
cd novahoosh-vision-inspector
```
________________________________________
2. Initialize Third-Party Submodules

YOLOv7 and SORT are maintained as Git submodules and are intentionally separated from the NOVAHOOSH application code.

Initialize them with:
```
git submodule update --init --recursive
```
After successful initialization, the following directories should exist:
```
third_party/
├── yolov7/
└── sort/
```
If the repository was cloned without submodules, the command above is required before running the application.
________________________________________
3. Install Python Dependencies

Install the project dependencies using:
```
pip install -r requirements.txt
```
The project does not use the Ultralytics package.
YOLOv7 is integrated directly through the dedicated third-party repository.
________________________________________
🖥️ NVIDIA / CUDA

The current prototype has been tested using:
```
CUDA 11.6
```
An NVIDIA GPU environment with compatible NVIDIA drivers and CUDA/PyTorch support is required for GPU inference.
The selected GPU device is configured through:
```
"device": "0"
```
The exact CUDA and PyTorch installation depends on the target NVIDIA hardware and operating environment.
For CUDA/PyTorch compatibility, refer to the official PyTorch installation documentation.
________________________________________
📦 Model Weights

Model weights are kept separately from the application source code.

Expected location:
```
weights/
└── yolov7.pt
```
The detector configuration points to the required model weight.
Model weights are not considered part of the NOVAHOOSH application source code.

________________________________________
▶️ Running the Demo

After installation, submodule initialization, and model preparation, run:
```
python src/main.py
```
The system starts the complete processing pipeline:
```
Input Video
     ↓
GetFrame
     ↓
Detector
     ↓
Tracker
     ↓
Visualization
```
The visualization window displays the processed frames in real time.
________________________________________
🎥 Demo Input

The current prototype can process a video file configured in:
```
src/config.py
Example:
"source": "demo/1.mp4"
A camera source can be integrated later using the same frame-acquisition interface.
```
________________________________________
🎥 Reference Video

The demonstration uses publicly available industrial reference footage.

**Original source:**  
[https://www.tiktok.com/@klein7325](https://www.tiktok.com/@klein7325/video/7668933041070312712)

The original footage belongs to its respective owner
and is used here only as reference/demo input.

The AI processing pipeline was independently developed
for this project.
________________________________________
⚙️ Configuration

Runtime parameters are controlled through:
```
src/config.py
```
Example:
```
CONFIG = {

    "source":
    "demo/1.mp4",

    "output":
    "demo/result_1.mp4",

    "weights":
    "weights/yolov7.pt",


    "yolo_repo":
    "third_party/yolov7",


    "device":
    "0",


    "img_size":
    640,


    "confidence":
    0.7,

    "fps":
    30,

    "display":
    True,

    "recording":
    True
}
```
Main Parameters
```
Parameter	Description
source	Input video or camera source
output	Processed output video
fps	Processing / recording frame rate
queue_size	Maximum queue size between processing stages
display	Enable real-time visualization
recording	Enable processed-video recording
confidence	Minimum detection confidence
device	CUDA device or CPU
```
________________________________________
🎯 Detection Confidence

Detection confidence can be controlled directly through:
```
"confidence": 0.25
For example:
"confidence": 0.70
```
requires a higher confidence before a detection is accepted for visualization.
This parameter allows the behavior of the detection stage to be adjusted without modifying the YOLOv7 source code.

________________________________________
🎥 Recording

Processed frames can be recorded by enabling:
```
"recording": True
The output file is defined by:
"output": "demo/result_1.mp4"
```
The recorded video contains the visualization output generated by the processing pipeline.

Example:
```
demo/
├── 1.mp4
└── result_1.mp4

When recording is disabled:
"recording": False
```
the system can operate without writing the processed frames to disk.

________________________________________
🛑 Stopping the Application
```
Press:
q
to stop the visualization.
```
The visualization component releases the video writer and closes OpenCV resources before stopping.
________________________________________
🔗 Object Tracking

The project uses SORT (Simple Online and Realtime Tracking) as the tracking backend.

The tracker is kept as an independent third-party component.

The current architecture allows detection results to be passed to the tracker without coupling the NOVAHOOSH application to the internal implementation of SORT.

The tracking stage provides the foundation for future functions such as:
```
•	Object identity across frames
•	Temporal consistency
•	Object counting
•	Inspection history
•	Defect decision over multiple frames
```
________________________________________
🏭 Industrial Inspection Concept

The initial application is beverage bottle-cap inspection.

A future production implementation can follow the architecture:
```
Industrial Camera
       │
       ▼
Real-Time Frame Acquisition
       │
       ▼
AI Detection
       │
       ▼
Object Tracking
       │
       ▼
Defect Analysis
       │
       ▼
Quality Decision
       │
       ▼
Accept / Reject
```
Potential inspection targets include:
```
•	Missing bottle caps
•	Incorrect cap placement
•	Damaged caps
•	Abnormal cap position
•	Packaging defects
•	Product appearance defects
```
The current repository demonstrates the computer-vision pipeline and is not presented as a certified production inspection system.
________________________________________
📊 Evaluation

Performance evaluation will be expanded as the prototype develops.

Planned metrics include:
```
Metric	Status
Detection Accuracy	In Development
Detection Confidence	Available
Processing FPS	In Development
Inference Latency	In Development
Tracking Stability	In Development
Defect Detection Accuracy	Planned
False Detection Rate	Planned
```
Performance depends on:
```
•	Detection model
•	Input resolution
•	GPU
•	Camera
•	Lighting conditions
•	Production-line speed
•	Object appearance
```
________________________________________
🧪 Current Prototype Scope

This project is intentionally limited to a focused technical demonstration.

The current prototype does not attempt to implement a complete industrial production system.

The primary objective is to demonstrate:
```
AI Detection
     +
Real-Time Processing
     +
Tracking Architecture
     +
Visualization
     +
Edge-AI Preparation
```
This approach allows the core technology to be demonstrated before introducing the complexity of complete industrial integration.
________________________________________
🛣️ Development Roadmap
```
Phase 1 — Vision Prototype
•	 Video input
•	 Multi-threaded frame processing
•	 YOLOv7 inference
•	 CUDA inference
•	 Configurable confidence threshold
•	 Detection visualization
•	 Processed-video recording
Phase 2 — Intelligent Inspection
•	 Tracking architecture
•	 Robust object tracking validation
•	 Temporal object analysis
•	 Bottle-cap defect classification
•	 Industrial OK / NG decision logic
•	 Performance metrics
Phase 3 — Edge AI
•	 NVIDIA Jetson deployment
•	 GStreamer-based camera pipeline
•	 Edge inference optimization
•	 Hardware-in-the-loop demonstration
Phase 4 — Industrial Integration
•	 Industrial camera integration
•	 PLC communication
•	 Automatic rejection mechanism
•	 Production statistics
•	 Multi-camera inspection
```
________________________________________
🧩 Third-Party Components

NOVAHOOSH Vision Inspector uses selected third-party projects as independent Git submodules.

They are intentionally kept outside the main application source code.
________________________________________
```
YOLOv7
YOLOv7 is used as the object-detection backend.
Official repository:
https://github.com/WongKinYiu/yolov7
YOLOv7 is distributed under the GNU General Public License v3.0 (GPL-3.0).
The original source code, copyright notices, and license remain associated with the third-party component.
The YOLOv7 project is not owned by NOVAHOOSH.
Reference:
C.-Y. Wang, A. Bochkovskiy, and H.-Y. M. Liao,
"YOLOv7: Trainable Bag-of-Freebies Sets New State-of-the-Art for Real-Time Object Detectors."
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2023.
Paper:
https://arxiv.org/abs/2207.02696
________________________________________
SORT
SORT is used as the object-tracking backend.
Official repository:
https://github.com/abewley/sort
SORT is released under the GPL License.
The original SORT source code, copyright notices, and license remain associated with the third-party component.
Reference:
A. Bewley, Z. Ge, L. Ott, F. Ramos, and B. Upcroft,
"Simple Online and Realtime Tracking."
IEEE International Conference on Image Processing (ICIP), 2016.
DOI:
https://doi.org/10.1109/ICIP.2016.7533003
```
________________________________________
📚 References
```
YOLOv7
Wang, Chien-Yao; Bochkovskiy, Alexey; Liao, Hong-Yuan Mark.
YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors.
CVPR, 2023.
Repository:
https://github.com/WongKinYiu/yolov7
Paper:
https://arxiv.org/abs/2207.02696
________________________________________
SORT
Bewley, Alex; Ge, Zongyuan; Ott, Lionel; Ramos, Fabio; Upcroft, Ben.
Simple Online and Realtime Tracking.
2016 IEEE International Conference on Image Processing (ICIP).
DOI:
https://doi.org/10.1109/ICIP.2016.7533003
Repository:
https://github.com/abewley/sort
________________________________________
PyTorch
The project uses PyTorch as the deep-learning inference framework.
Official documentation:
https://pytorch.org/
CUDA-compatible PyTorch installation information:
https://pytorch.org/get-started/previous-versions/
________________________________________
OpenCV
OpenCV is used for image acquisition, image processing, visualization, and video handling.
Official repository:
https://github.com/opencv/opencv
```
________________________________________
⚖️ Third-Party License Policy

Third-party components remain subject to their respective original licenses.
NOVAHOOSH does not claim ownership of third-party source code.

The following components are maintained separately from the NOVAHOOSH application code:
```
third_party/yolov7/
third_party/sort/
Their original license files and notices must remain available.
Before redistributing or commercially deploying the complete software stack, the applicable licenses of all third-party components must be reviewed and respected.
```
________________________________________
⚠️ Prototype Notice

This repository represents a research and engineering prototype.
It is intended to demonstrate the architecture and technical feasibility of AI-based industrial visual inspection.
The current implementation has not been validated as a production-certified inspection system.

Real industrial deployment requires additional validation, including:
```
•	Camera and lighting optimization
•	Dataset validation
•	Production-line testing
•	False-positive / false-negative analysis
•	Hardware reliability testing
•	Safety and control integration
•	Acceptance testing
```
________________________________________
🏢 About NOVAHOOSH

NOVAHOOSH develops intelligent engineering systems based on:
```
•	Artificial Intelligence
•	Computer Vision
•	Embedded Systems
•	Robotics
•	Industrial Automation
•	Advanced Control
```
Our goal is to transform conventional production processes into intelligent, data-driven systems.
________________________________________
🤝 Industrial Collaboration
```
NOVAHOOSH Vision Inspector is designed as a foundation for developing customized industrial inspection solutions.
The architecture can be adapted to different:
•	Products
•	Cameras
•	Production lines
•	Inspection requirements
•	Edge-computing platforms
```
For industrial cooperation and customized AI vision solutions:NOVAHOOSH
________________________________________
📄 License
```
The NOVAHOOSH application code in this repository is proprietary unless otherwise stated.
Third-party components remain subject to their respective original licenses.
In particular:
•	YOLOv7 → GPL-3.0
•	SORT → GPL
Please review the individual license files contained within:
third_party/
before redistributing or commercially deploying the complete software stack.
```
________________________________________
@ NOVAHOOSH

AI • Computer Vision • Industrial Intelligence
Building intelligent vision systems for real-world production