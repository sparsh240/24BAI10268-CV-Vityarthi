# Statement

## Problem Statement

Many image-processing tasks require identifying the geometric shapes present in an image. Manually detecting shapes is time-consuming and error-prone, especially when the image contains multiple objects with different sizes and orientations. This project addresses that challenge by automatically detecting and classifying basic geometric shapes from a given image.

## Scope of the Project

The scope of this project includes image loading, preprocessing, contour detection, shape classification, boundary drawing, and output generation. The project focuses on common geometric shapes such as triangle, square, rectangle, circle, and polygon.

The system is designed for a controlled image environment where the target objects are clearly visible and separated from the background. It is not intended to handle highly complex real-world scenes with overlapping objects or noisy backgrounds without additional tuning.

## Target Users

This project is useful for:

- Students learning computer vision and image processing
- Beginners exploring OpenCV and contour detection
- Small projects or demos involving basic shape recognition
- Educational applications that require object identification from images

## High-Level Features

- Input image loading from the local project folder
- Conversion to grayscale and preprocessing for better contour extraction
- Edge and contour detection using OpenCV
- Shape recognition for common geometric forms
- Bounding box and label overlays on detected shapes
- Saving the final annotated image as output
