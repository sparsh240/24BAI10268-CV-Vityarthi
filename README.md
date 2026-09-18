# Vityarthi Shape Detection Project

## Overview

This project detects and classifies basic geometric shapes from an input image. It reads an image file, identifies contours, labels each detected object, and saves an annotated output image for later review.

The system is designed for simple image-processing tasks and is useful for understanding how OpenCV contour detection and shape recognition can be applied in real-world vision workflows.

## Features

- Detects objects from an input image using contour analysis
- Classifies common shapes such as triangle, rectangle, square, circle, and polygon
- Draws labeled bounding boxes and outlines around detected objects
- Saves the output image in the project output folder
- Works with a local virtual environment for clean dependency management

## Technologies and Tools Used

- Python 3
- OpenCV (cv2)
- NumPy
- Virtual environment for dependency isolation
- Git and GitHub for repository management

## Project Structure

- [main.py](main.py) — main script for image loading, detection, and saving the result
- [requirements.txt](requirements.txt) — project dependencies
- [images/inputs/image.png](images/inputs/image.png) — sample input image
- [images/outputs/detected_objects.jpg](images/outputs/detected_objects.jpg) — generated output image
- [env/](env/) — local Python environment

## Installation and Setup

### 1. Clone or open the project

Open a terminal in the project folder:

```bash
cd /home/sparsh/Work/Vityarthi
```

### 2. Create a virtual environment

```bash
python3 -m venv env
```

Activate it:

Linux/macOS:

```bash
source env/bin/activate
```

Windows PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The required dependencies are already listed in [requirements.txt](requirements.txt):

- numpy
- opencv-python

## Configuration

The project uses the following default paths:

- Input image: [images/inputs/image.png](images/inputs/image.png)
- Output image: [images/outputs/detected_objects.jpg](images/outputs/detected_objects.jpg)

These paths are defined in [main.py](main.py). If you want to use a different image, update the file path variables at the top of the script.

## How to Run

From the project root, run:

```bash
python main.py
```

Or, using the local environment directly:

```bash
./env/bin/python main.py
```

## Testing

To verify the project runs correctly:

1. Ensure the input image exists in [images/inputs/image.png](images/inputs/image.png).
2. Run the program using the command above.
3. Check the console output for detected shapes.
4. Confirm that the annotated image is saved in [images/outputs/detected_objects.jpg](images/outputs/detected_objects.jpg).

Example output in the terminal should list detected object names such as triangle, square, rectangle, circle, and polygon.


## Troubleshooting

### ModuleNotFoundError: No module named 'cv2'

Install the dependencies again:

```bash
pip install -r requirements.txt
```

### Input image not found

Check that [images/inputs/image.png](images/inputs/image.png) exists and that the path in [main.py](main.py) matches it.

### No shapes detected

The project uses contour thresholding and edge filtering. If you replace the sample image, you may need to adjust the detection threshold values in [main.py](main.py) for better results.

## Summary

This project demonstrates a simple but effective computer vision workflow: preprocessing an image, detecting shape boundaries, classifying each form, and saving a labeled result. It is useful as a beginner-friendly introduction to OpenCV-based image analysis.
