# main.py
"""
HomeTeam Network - AI Engineer Take-Home Project
Sports Motion Detection & Viewport Tracking

This is the main entry point for the motion detection and viewport tracking program.
"""

import os
import argparse
import cv2
import numpy as np

from frame_processor import process_video
from motion_detector import detect_motion
from viewport_tracker import track_viewport
from visualizer import visualize_results


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Sports Motion Detection & Viewport Tracking"
    )
    parser.add_argument(
        "--video", type=str, required=True, help="Path to input video file"
    )
    parser.add_argument("--output", type=str, default="output", help="Output directory")
    parser.add_argument("--fps", type=int, default=5, help="Target frames per second")
    parser.add_argument(
        "--viewport_size",
        type=str,
        default="720x480",
        help="Size of viewport in format WIDTHxHEIGHT",
    )
    return parser.parse_args()


def main():
    """Main function to run the motion detection and viewport tracking pipeline."""
    # Parse arguments
    args = parse_args()

    # Parse viewport size
    try:
        viewport_width, viewport_height = map(int, args.viewport_size.split("x"))
        viewport_size = (viewport_width, viewport_height)
    except ValueError:
        print(
            f"Invalid viewport size format: {args.viewport_size}. Using default 720x480."
        )
        viewport_size = (720, 480)

    # Create output directory if it doesn't exist
    os.makedirs(args.output, exist_ok=True)

    print(f"Processing video: {args.video}")

    # Step 1: Extract frames from video
    frames = process_video(args.video, args.fps)
    print(f"Extracted {len(frames)} frames")

    # Step 2: Detect motion in frames
    motion_results = []
    for i, frame in enumerate(frames):
        print(f"Processing frame {i + 1}/{len(frames)}")

        # Pass the entire frames list and the current index to detect_motion
        motion_boxes = detect_motion(frames, i)
        motion_results.append(motion_boxes)

    # Step 3: Track viewport based on motion detection
    viewport_positions = track_viewport(frames, motion_results, viewport_size)

    # Step 4: Visualize and save results
    visualize_results(
        frames, motion_results, viewport_positions, viewport_size, args.output
    )

    print(f"Processing complete. Results saved to {args.output}")


if __name__ == "__main__":
    main()

# frame_processor.py
"""
Frame processing functions for the motion detection project.
"""

import cv2
import numpy as np


def process_video(video_path, target_fps=5, resize_dim=(1280, 720)):
    """
    Extract frames from a video at a specified frame rate.

    Args:
        video_path: Path to the video file
        target_fps: Target frames per second to extract
        resize_dim: Dimensions to resize frames to (width, height)

    Returns:
        List of extracted frames
    """
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")

    # Get video properties
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate frame interval for the target FPS
    frame_interval = max(1, int(original_fps / target_fps))

    # TODO: Implement frame extraction
    # 1. Read frames from the video capture object
    # 2. Only keep frames at the specified interval to achieve target_fps
    # 3. Resize frames to the specified dimensions
    # 4. Store frames in a list
    # 5. Release the video capture object when done

    # Example starter code:
    frames = []
    frame_index = 0

    # Your implementation here

    return frames


# motion_detector.py
"""
Motion detection functions for the sports video analysis project.
"""

import cv2
import numpy as np


def detect_motion(frames, frame_idx, threshold=25, min_area=100):
    """
    Detect motion in the current frame by comparing with previous frame.

    Args:
        frames: List of video frames
        frame_idx: Index of the current frame
        threshold: Threshold for frame difference detection
        min_area: Minimum contour area to consider

    Returns:
        List of bounding boxes for detected motion regions
    """
    # We need at least 2 frames to detect motion
    if frame_idx < 1 or frame_idx >= len(frames):
        return []

    # Get current and previous frame
    current_frame = frames[frame_idx]
    prev_frame = frames[frame_idx - 1]

    # TODO: Implement motion detection
    # 1. Convert frames to grayscale
    # 2. Apply Gaussian blur to reduce noise (hint: cv2.GaussianBlur)
    # 3. Calculate absolute difference between frames (hint: cv2.absdiff)
    # 4. Apply threshold to highlight differences (hint: cv2.threshold)
    # 5. Dilate the thresholded image to fill in holes (hint: cv2.dilate)
    # 6. Find contours in the thresholded image (hint: cv2.findContours)
    # 7. Filter contours by area and extract bounding boxes

    # Example starter code:
    motion_boxes = []

    # Your implementation here

    return motion_boxes


# viewport_tracker.py
"""
Viewport tracking functions for creating a smooth "virtual camera".
"""

import cv2
import numpy as np


def calculate_region_of_interest(motion_boxes, frame_shape):
    """
    Calculate the primary region of interest based on motion boxes.

    Args:
        motion_boxes: List of motion detection bounding boxes
        frame_shape: Shape of the video frame (height, width)

    Returns:
        Tuple (x, y, w, h) representing the region of interest center point and dimensions
    """
    # TODO: Implement region of interest calculation
    # 1. Choose a strategy for determining the main area of interest
    #    - You could use the largest motion box
    #    - Or combine nearby boxes
    #    - Or use a weighted average of all motion boxes
    # 2. Return the coordinates of the chosen region

    # Example starter code:
    if not motion_boxes:
        # If no motion is detected, use the center of the frame
        height, width = frame_shape[:2]
        return (width // 2, height // 2, 0, 0)

    # Your implementation here

    return (0, 0, 0, 0)  # Placeholder


def track_viewport(frames, motion_results, viewport_size, smoothing_factor=0.3):
    """
    Track viewport position across frames with smoothing.

    Args:
        frames: List of video frames
        motion_results: List of motion detection results for each frame
        viewport_size: Tuple (width, height) of the viewport
        smoothing_factor: Factor for smoothing viewport movement (0-1)
                          Lower values create smoother movement

    Returns:
        List of viewport positions for each frame as (x, y) center coordinates
    """
    # TODO: Implement viewport tracking with smoothing
    # 1. For each frame, determine the region of interest based on motion_results
    # 2. Apply smoothing to avoid jerky movements
    #    - Use previous viewport positions to smooth the movement
    #    - Consider implementing a simple exponential moving average
    #    - Or a more advanced approach like Kalman filtering
    # 3. Ensure the viewport stays within the frame boundaries
    # 4. Return the list of viewport positions for all frames

    # Example starter code:
    viewport_positions = []

    # Initialize with center of first frame if available
    if frames:
        height, width = frames[0].shape[:2]
        prev_x, prev_y = width // 2, height // 2
    else:
        return []

    # Your implementation here

    return viewport_positions


# visualizer.py
"""
Visualization functions for displaying motion detection and viewport tracking results.
"""

import os
import cv2
import numpy as np


def visualize_results(
    frames, motion_results, viewport_positions, viewport_size, output_dir
):
    """
    Create visualization of motion detection and viewport tracking results.

    Args:
        frames: List of video frames
        motion_results: List of motion detection results for each frame
        viewport_positions: List of viewport center positions for each frame
        viewport_size: Tuple (width, height) of the viewport
        output_dir: Directory to save visualization results
    """
    # Create output directory for frames
    frames_dir = os.path.join(output_dir, "frames")
    os.makedirs(frames_dir, exist_ok=True)

    viewport_dir = os.path.join(output_dir, "viewport")
    os.makedirs(viewport_dir, exist_ok=True)

    # Get dimensions for the output video
    height, width = frames[0].shape[:2]

    # Create video writers
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_path = os.path.join(output_dir, "motion_detection.mp4")
    video_writer = cv2.VideoWriter(video_path, fourcc, 5, (width, height))

    viewport_video_path = os.path.join(output_dir, "viewport_tracking.mp4")
    vp_width, vp_height = viewport_size
    viewport_writer = cv2.VideoWriter(
        viewport_video_path, fourcc, 5, (vp_width, vp_height)
    )

    # TODO: Implement visualization
    # 1. Process each frame
    #    a. Create a copy of the frame for visualization
    #    b. Draw bounding boxes around motion regions
    #       (hint: cv2.rectangle with green color (0, 255, 0))
    #    c. Draw the viewport rectangle
    #       (hint: cv2.rectangle with blue color (255, 0, 0))
    #    d. Extract the viewport content (the area inside the viewport)
    #    e. Add frame number to the visualization (hint: cv2.putText)
    #    f. Save visualization frames and viewport frames as images
    #    g. Write frames to both video writers
    # 2. Release the video writers when done

    # Example starter code:
    for i, frame in enumerate(frames):
        # Your implementation here
        pass

    print(f"Visualization saved to {video_path}")
    print(f"Viewport video saved to {viewport_video_path}")
    print(f"Individual frames saved to {frames_dir} and {viewport_dir}")
