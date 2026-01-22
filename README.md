# Sharp-Shot Video Filter

This project is a solution for the Computer Vision Internship Technical Challenge. It processes a video file to identify and extract the **Top 5 sharpest frames**, ensuring they are temporally diverse (not from the same second).

## Features
- **Sharpness Detection:** Uses the Laplacian Variance method to quantify image clarity.
- **Temporal Diversity:** Implements a greedy selection algorithm to ensure selected frames are spread across the video duration.
- **Efficiency:** Analyzes frames sequentially and only re-reads the high-quality data for the final selection to optimize memory usage.

## Prerequisites
Ensure you have Python 3.x installed. You will need the `opencv-python`  library.

## Installation
1. Clone or download this project folder.
2. Install the required dependencies:
   ```bash
   pip install opencv
   ```

## How to Run
since this version uses manual path configuration for better control during development, follow these steps:
1.Open the sharp_shot.py file in your code editor.
2.Locate the if __name__ == "__main__": block at the bottom.
3.Manually update the video_path and output_folder variables with your local file paths:

### Optional Arguments
- `--output`: Specify the directory to save the frames (default: `output`).
- `--n`: Number of frames to extract (default: `5`).
- `--interval`: Minimum seconds between frames (default: `1.0`).

Example:
```bash
python sharp_shot.py my_video.mp4 --n 5 --interval 2.0
```

## Project Structure
- `sharp_shot.py`: The main Python implementation.
- `docs/explanation.md`: Detailed mathematical explanation of the Laplacian Variance method and the diversity logic.
- `output/`: Directory where the sharpest frames will be saved.
