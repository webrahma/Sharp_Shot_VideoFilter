The Most Difficult Decision: Balancing Memory Management vs. Processing Speed
During the development of the Sharp-Shot filter, the most challenging technical decision was determining how to handle video frames during the analysis phase without exhausting system resources.

1. The Problem: Initially, the straightforward approach was to store every frame from the video in a Python list along with its sharpness score. However, for high-definition or long-duration videos, this would lead to massive RAM consumption, potentially causing the system to crash or significantly slow down during the sorting process.

2. The Decision (Metadata-First Approach): I decided to implement a dual-pass processing strategy:

First Pass (Analysis): The script iterates through the video to calculate the Laplacian Variance for each frame. Instead of storing the actual image data, it only stores a lightweight dictionary containing the frame index, timestamp, and sharpness score.

Second Pass (Extraction): Once the Top 5 diverse frames are identified using the temporal constraint logic, the script uses cv2.CAP_PROP_POS_FRAMES to jump directly to those specific indices and read only the required frames for saving.

3. The Outcome: This decision involved a minor trade-off in processing time (as we access the video file twice), but it resulted in a highly efficient and "production-ready" script. The tool can now handle large video files smoothly on machines with limited RAM while maintaining 100% accuracy in identifying the sharpest frames.
