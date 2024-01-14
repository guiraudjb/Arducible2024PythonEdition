#!/bin/bash
python3 -mvenv ../pythonvenv
source ../pythonvenv/bin/activate
pip3 install opencv-python numpy mediapipe pygame
python3 main.py
