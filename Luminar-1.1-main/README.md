#  Adaptive-brightness-app V 1.0

## Overview
This script dynamically adjusts the brightness of your display based on the content captured from your webcam. It uses OpenCV to capture images from the webcam and the Pillow library to process these images. The brightness of the display is adjusted to optimize visibility according to the ambient lighting conditions detected in the webcam feed.

## Features
- **Webcam Image Capture**: Utilizes the system's webcam to continuously capture images.
- **Image Processing**: Converts images to grayscale, enhances contrast, and applies adaptive thresholding to detect bright areas.
- **Brightness Calculation**: Calculates the percentage of bright pixels in the processed image and adjusts the screen brightness based on this calculation.
- **Brightness Adjustment**: Uses PowerShell commands to set the screen brightness on Windows systems.

## Requirements
- Python 3.x
- OpenCV-Python (`opencv-python`)
- Pillow (`Pillow`)
- NumPy (`numpy`)

## Installation
1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install the required Python libraries using pip:
   ```bash
   pip install opencv-python Pillow numpy
