import numpy as np
import cv2

frame = cv2.imread("4.jpg")  # Read image from file (for testing).

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Use BGR to Gray conversion (not RGBA, because image is read from file)

# Apply adaptiveThreshold with large filter size.
thres_gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 51, 2)

# Find contours (external contours)
cnts, hier = cv2.findContours(thres_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Find contour with the maximum area
c = max(cnts, key=cv2.contourArea)

res = np.zeros_like(gray)  # Create new zeros images for storing the result.

# Fill the contour with white color - draw the filled contour on res image.
cv2.drawContours(res, [c], -1, 255, -1)

# Compute the center of the contour
# https://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour/
M = cv2.moments(c)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

# Use floodFill for filling the center of the contour
cv2.floodFill(res, None, (cX, cY), 255)

# Show images for testing
cv2.imshow('thres_gray', thres_gray)
cv2.imshow('res', res)
cv2.waitKey()
cv2.destroyAllWindows()
