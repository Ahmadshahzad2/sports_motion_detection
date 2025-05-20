"""
Viewport tracking functions for creating a smooth "virtual camera".
"""

import numpy as np


def _union_box(boxes):
    xs, ys, ws, hs = zip(*boxes)
    x0, y0 = min(xs), min(ys)
    x1 = max(xs[i] + ws[i] for i in range(len(boxes)))
    y1 = max(ys[i] + hs[i] for i in range(len(boxes)))
    return x0, y0, x1 - x0, y1 - y0


def calculate_region_of_interest(motion_boxes, frame_shape):
    """
    Pick the **union** of all motion boxes; falls back to frame-center if none.
    """
    h, w = frame_shape[:2]
    if not motion_boxes:
        return w // 2, h // 2, 0, 0

    x, y, bw, bh = _union_box(motion_boxes)
    cx = x + bw // 2
    cy = y + bh // 2
    return cx, cy, bw, bh


def track_viewport(frames, motion_results, viewport_size, smoothing_factor: float = 0.3):
    """
    Returns:
        List[tuple[int, int]] viewport center (cx, cy) for every frame
    """
    if not frames:
        return []

    h, w = frames[0].shape[:2]
    vp_w, vp_h = viewport_size

    cx_prev, cy_prev = w // 2, h // 2
    positions = []

    for boxes in motion_results:
        cx_tgt, cy_tgt, _, _ = calculate_region_of_interest(boxes, frames[0].shape)

        # EMA smoothing
        cx = int(smoothing_factor * cx_tgt + (1 - smoothing_factor) * cx_prev)
        cy = int(smoothing_factor * cy_tgt + (1 - smoothing_factor) * cy_prev)

        # keep viewport inside frame bounds
        cx = max(vp_w // 2, min(cx, w - vp_w // 2))
        cy = max(vp_h // 2, min(cy, h - vp_h // 2))

        positions.append((cx, cy))
        cx_prev, cy_prev = cx, cy

    return positions
