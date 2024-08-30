# scripts/motion_simulator.py

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    from .mock_gpio import GPIO

import time

def simulate_motion_detection():
    print("Simulating motion detection...")
    time.sleep(2)
    print("Motion detected!")
