
# SmartDrive — Autonomous Robotic Vehicle

## Project Overview

SmartDrive is an academic robotics project developed as part of
the Master's program in Computer Engineering and Embedded Systems
(IISE).

The project aims to design and develop a miniature autonomous
robotic vehicle capable of perceiving its environment and
adapting its driving behavior using computer vision,
artificial intelligence, and embedded control.

## Main Objectives

- Autonomous lane detection and following
- Automatic navigation through curves
- STOP sign recognition
- Speed-limit recognition (20, 40, 60)
- Adaptive speed control using wheel encoders
- Obstacle detection and automatic stopping
- Real-time visualization and monitoring

## Proposed Hardware

- Raspberry Pi 4 (4 GB RAM)
- Raspberry Pi Camera
- ESP32 microcontroller
- Two DC motors with wheel encoders
- Motor driver
- Ultrasonic distance sensor
- Robotic chassis and power supply

## Software and Technologies

- Python
- OpenCV
- YOLO or an appropriate lightweight AI model
- NumPy
- Raspberry Pi OS
- ESP32 firmware
- Git and GitHub

## System Architecture

Camera → Raspberry Pi → ESP32 → Motor Driver → Motors

The Raspberry Pi processes images and determines driving
commands. The ESP32 is responsible for motor control,
encoder measurements, and local safety functions.

## Current Development Status

Project in development.

Completed:
- Python development environment configured
- OpenCV and NumPy installed
- Laptop webcam capture tested
- Initial image-thresholding experiment implemented

In progress / planned:
- Raspberry Pi camera integration
- Lane detection and steering calculation
- Traffic-sign recognition
- ESP32 communication and motor control
- System integration and experimental validation

## Academic Context

Master IISE — Ingénierie Informatique et Systèmes Embarqués

Module: Vision Robotique et Artificielle

Team: Five students

## Project Note

SmartDrive is an educational prototype intended for use on
a controlled miniature test track, not on public roads.
