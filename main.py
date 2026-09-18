import math
import os
from pathlib import Path

import cv2
import numpy as np

# ------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "images" / "inputs" / "image.png"
OUTPUT_PATH = BASE_DIR / "images" / "outputs" / "detected_objects.jpg"
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

MIN_AREA = 500


# ------------------------------------------------------------
# LOAD IMAGE
# ------------------------------------------------------------

image = cv2.imread(str(IMAGE_PATH))

if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

# Keep original for drawing
output = image.copy()


# ------------------------------------------------------------
# PREPROCESSING
# ------------------------------------------------------------

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find the dark object outlines while ignoring the white background and outer frame.
# A low threshold keeps the actual shape edges but excludes the large border region.
_, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)

# Clean up small gaps and smooth the object outlines
kernel = np.ones((3, 3), np.uint8)
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)


# ------------------------------------------------------------
# FIND OBJECT CONTOURS
# ------------------------------------------------------------

contours, _ = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)


detected_objects = []


# ------------------------------------------------------------
# PROCESS EACH OBJECT
# ------------------------------------------------------------

for contour in contours:
    area = cv2.contourArea(contour)

    # Ignore small noise and the outer image border
    if area < MIN_AREA:
        continue

    x, y, w, h = cv2.boundingRect(contour)
    image_h, image_w = image.shape[:2]

    if x <= 2 or y <= 2 or x + w >= image_w - 2 or y + h >= image_h - 2:
        continue

    if area > 0.9 * image_w * image_h:
        continue

    perimeter = cv2.arcLength(contour, True)

    if perimeter == 0:
        continue

    approximation = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
    vertices = len(approximation)

    # --------------------------------------------------------
    # SHAPE CLASSIFICATION
    # --------------------------------------------------------

    if vertices == 3:
        shape = "Triangle"

    elif vertices == 4:
        aspect_ratio = w / float(h) if h > 0 else 0.0

        if 0.90 <= aspect_ratio <= 1.10:
            shape = "Square"
        else:
            shape = "Rectangle"

    elif vertices > 4:
        circularity = (4 * math.pi * area) / (perimeter * perimeter)

        if circularity > 0.75:
            shape = "Circle"
        else:
            shape = "Polygon"

    else:
        shape = "Unknown"

    detected_objects.append(shape)

    cv2.drawContours(output, [contour], -1, (0, 255, 0), 2)
    cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(output, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


# ------------------------------------------------------------
# PRINT RESULTS
# ------------------------------------------------------------

print("\nDetected objects:")

if len(detected_objects) == 0:
    print("No objects detected.")
else:
    for i, obj in enumerate(detected_objects, start=1):
        print(f"{i}. {obj}")


# ------------------------------------------------------------
# SAVE RESULT
# ------------------------------------------------------------

saved = cv2.imwrite(str(OUTPUT_PATH), output)
if not saved:
    raise IOError(f"Failed to save output image to {OUTPUT_PATH}")

print(f"\nResult saved as: {OUTPUT_PATH}")


