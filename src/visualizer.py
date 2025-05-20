"""
Visualization functions for displaying motion detection and viewport tracking results.
"""

import os
import cv2


def _draw_boxes(frame, boxes, color=(0, 255, 0)):
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 1)


def _draw_viewport(frame, center, vp_size, color=(255, 0, 0)):
    cx, cy = center
    vw, vh = vp_size
    x0, y0 = cx - vw // 2, cy - vh // 2
    x1, y1 = x0 + vw, y0 + vh
    cv2.rectangle(frame, (x0, y0), (x1, y1), color, 2)


def visualize_results(frames, motion_results, viewport_positions, viewport_size, output_dir):
    """
    Save annotated full-frame video and viewport-only video (+JPGs).
    """
    os.makedirs(output_dir,         exist_ok=True)
    frames_dir   = os.path.join(output_dir, "frames")
    viewport_dir = os.path.join(output_dir, "viewport")
    os.makedirs(frames_dir,   exist_ok=True)
    os.makedirs(viewport_dir, exist_ok=True)

    h, w = frames[0].shape[:2]
    vw, vh = viewport_size
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    full_out_path = os.path.join(output_dir, "motion_detection.mp4")
    vp_out_path   = os.path.join(output_dir, "viewport_tracking.mp4")

    full_writer = cv2.VideoWriter(full_out_path, fourcc, 5, (w, h))
    vp_writer   = cv2.VideoWriter(vp_out_path,   fourcc, 5, (vw, vh))

    for idx, (frame, boxes, center) in enumerate(zip(frames, motion_results, viewport_positions)):
        vis = frame.copy()
        _draw_boxes(vis, boxes)
        _draw_viewport(vis, center, viewport_size)

        # Add frame number
        cv2.putText(vis, f"Frame {idx+1}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        # Save annotated full frame
        full_path = os.path.join(frames_dir, f"vis_{idx:04d}.jpg")
        cv2.imwrite(full_path, vis)
        full_writer.write(vis)

        # Extract and save viewport crop
        cx, cy   = center
        x0, y0   = cx - vw // 2, cy - vh // 2
        crop     = frame[y0:y0 + vh, x0:x0 + vw]
        vp_path  = os.path.join(viewport_dir, f"crop_{idx:04d}.jpg")
        cv2.imwrite(vp_path, crop)
        vp_writer.write(crop)

    full_writer.release()
    vp_writer.release()

    print(f"Visualization saved to {full_out_path}")
    print(f"Viewport video saved to {vp_out_path}")
    print(f"Individual frames saved under {frames_dir} and {viewport_dir}")
