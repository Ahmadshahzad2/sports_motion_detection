
"""
Frame processing functions for the motion detection project.
"""

import cv2


def process_video(video_path, target_fps: int = 5, resize_dim: tuple[int, int] = (1280, 720)):
    """
    Extract frames from a video at a specified frame rate.

    Args:
        video_path: Path to the video file
        target_fps: Target frames per second to extract
        resize_dim: Dimensions to resize frames to (width, height)

    Returns:
        List[ndarray]: extracted & resized BGR frames
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")

    # Video properties
    src_fps = cap.get(cv2.CAP_PROP_FPS) or 30
    step = max(1, int(src_fps / target_fps))

    frames = []
    idx = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if idx % step == 0:                        # keep only required frames
            frame = cv2.resize(frame, resize_dim, interpolation=cv2.INTER_AREA)
            frames.append(frame)
        idx += 1

    cap.release()
    return frames
