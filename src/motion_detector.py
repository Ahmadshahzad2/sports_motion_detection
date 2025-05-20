"""
Motion detection functions for the sports video analysis project.
"""

import cv2
import numpy as np


def detect_motion(frames, frame_idx: int, threshold: int = 25, min_area: int = 500):
    """
    Detect motion in the current frame by comparing with the previous frame.

    Returns:
        List[tuple[int,int,int,int]] : bounding boxes (x, y, w, h)
    """
    if frame_idx < 1 or frame_idx >= len(frames):
        return []

    cur = cv2.cvtColor(frames[frame_idx],     cv2.COLOR_BGR2GRAY)
    prev = cv2.cvtColor(frames[frame_idx - 1], cv2.COLOR_BGR2GRAY)

    # smoothing to reduce false positives
    cur_blur  = cv2.GaussianBlur(cur,  (5, 5), 0)
    prev_blur = cv2.GaussianBlur(prev, (5, 5), 0)

    diff = cv2.absdiff(cur_blur, prev_blur)
    _, th = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    th = cv2.dilate(th, None, iterations=2)

    contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes: list[tuple[int, int, int, int]] = []

    for c in contours:
        if cv2.contourArea(c) < min_area:
            continue
        x, y, w, h = cv2.boundingRect(c)
        boxes.append((x, y, w, h))

    return boxes
