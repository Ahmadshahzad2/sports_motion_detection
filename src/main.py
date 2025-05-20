"""
HomeTeam Network - AI Engineer Take-Home Project
Sports Motion Detection & Viewport Tracking
"""

import os
import argparse

from frame_processor   import process_video
from motion_detector   import detect_motion
from viewport_tracker  import track_viewport
from visualizer        import visualize_results


def parse_args():
    p = argparse.ArgumentParser(description="Sports Motion Detection & Viewport Tracking")
    p.add_argument("--video",  required=True, help="Path to input video file")
    p.add_argument("--output", default="output", help="Output directory")
    p.add_argument("--fps",    default=5,  type=int, help="Target frames per second")
    p.add_argument("--viewport_size", default="720x480", help="WIDTHxHEIGHT (e.g. 720x480)")
    return p.parse_args()


def main():
    args = parse_args()

    try:
        vp_w, vp_h = map(int, args.viewport_size.lower().split("x"))
    except ValueError:
        print("Invalid viewport size; using 720x480")
        vp_w, vp_h = 720, 480
    viewport_size = (vp_w, vp_h)

    os.makedirs(args.output, exist_ok=True)

    # 1. frames
    frames = process_video(args.video, args.fps)
    print(f"Extracted {len(frames)} frames")

    # 2. motion detection
    motion_results = [detect_motion(frames, idx) for idx in range(len(frames))]

    # 3. viewport tracking
    viewport_positions = track_viewport(frames, motion_results, viewport_size)

    # 4. visualisation
    visualize_results(frames, motion_results, viewport_positions,
                      viewport_size, args.output)

    print("✅  Done.")


if __name__ == "__main__":
    main()
