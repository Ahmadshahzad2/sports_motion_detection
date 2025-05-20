# Sports Motion Detection & Viewport Tracking

*HomeTeam Network – AI Engineer Take-Home Project*


## Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [CLI Options](#cli-options)
6. [How It Works](#how-it-works)
7. [Tuning Hyper-parameters](#tuning-hyper-parameters)
8. [Sample Results](#sample-results)
9. [Future Improvements](#future-improvements)
10. [License](#license)


## Overview

This repository contains a lightweight Python pipeline that:

1. **Down-samples** a sports video to a small, uniform frame set
2. **Detects motion** frame-to-frame via classic image differencing
3. **Tracks** the primary action with a smooth “virtual camera” (viewport)
4. **Visualises** both the annotated full frame and the cropped viewport, saving:

   * `motion_detection.mp4` — broadcast-style feed with overlays
   * `viewport_tracking.mp4` — the smooth, cropped action feed
   * Individual JPEGs for debugging

The entire run finishes in seconds on a 10 s clip and uses **pure OpenCV**—no deep-learning weights or GPUs required.


## Project Structure

```
htn-viewport-tracker/
├─ src/
│  ├─ main.py              # command-line entry point
│  ├─ frame_processor.py   # frame extraction / resizing
│  ├─ motion_detector.py   # frame-difference based motion boxes
│  ├─ viewport_tracker.py  # EMA-smoothed virtual camera logic
│  └─ visualizer.py        # draws overlays & writes videos
├─ assets/                 # put sample.mp4 here (not committed)
├─ outputs/                # auto-generated results (git-ignored)
├─ requirements.txt
└─ README.md
```


## Installation

```bash
git clone 
cd hometeam_ai_assignment
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt      # opencv-python, numpy, tqdm, ffmpeg-python
```


## Quick Start

```bash
# place your 10-second clip under assets/
python -m src.main \
       --video assets/sample.mp4 \
       --output outputs \
       --fps 5 \
       --viewport_size 720x480
```

Look inside `outputs/` for two MP4s and per-frame JPGs.


## CLI Options

| Flag              | Default      | Description                  |
| ----------------- | ------------ | ---------------------------- |
| `--video`         | **required** | Path to input .mp4           |
| `--output`        | `output`     | Directory for results        |
| `--fps`           | `5`          | Target extraction frame-rate |
| `--viewport_size` | `720x480`    | WxH of virtual camera        |


## How It Works

1. **Frame Extraction** – keep 1 in ⌈src\_fps / target\_fps⌉ frames, resize to 1280×720.
2. **Motion Detection**

   * Grayscale → Gaussian blur → `absdiff(prev, curr)`
   * Binary threshold (>25) → dilation → contour finding
   * Filter small blobs (<500 px) → list of (x, y, w, h) boxes
3. **Region of Interest** – union of all boxes → centre point.
4. **Viewport Smoothing** – Exponential Moving Average
   `center_s = α * center_target + (1-α) * center_prev` with α = 0.3
5. **Bounds Clamping** – keeps rectangle inside full frame.
6. **Visualisation** – draw green motion boxes + blue viewport, label frame #, crop viewport, write both streams to MP4.


## Tuning Hyper-parameters

| Parameter          | Location                | Effect                                     |
| ------------------ | ----------------------- | ------------------------------------------ |
| `--fps`            | CLI / `frame_processor` | Runtime vs temporal resolution             |
| `threshold`        | `motion_detector`       | Motion sensitivity (15–30 recommended)     |
| `min_area`         | `motion_detector`       | Ignore tiny specks (<500 px²)              |
| `smoothing_factor` | `viewport_tracker`      | 0 = instant, 0.4 = snappy, 0.1 = cinematic |
| `--viewport_size`  | CLI                     | Zoom level of virtual camera               |


## Sample Results

After running the quick start you will have:

* **motion\_detection.mp4** – original resolution, green motion boxes, blue viewport
* **viewport\_tracking.mp4** – 720×480 feed that smoothly follows the play
* `outputs/frames/*.jpg` – one annotated image per kept frame
* `outputs/viewport/*.jpg` – cropped viewport JPGs

