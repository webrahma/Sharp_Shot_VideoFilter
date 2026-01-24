import cv2
import os

def calculate_sharpness(image):
    """
    Calculates the sharpness of an image using the Variance of Laplacian method.
    The Laplacian operator highlights regions of an image containing rapid intensity changes.
    A higher variance indicates a sharper image with more edges.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

def process_video(video_path, output_dir, top_n=5, min_interval_sec=1.0):
    """
    Processes the video to find the top N sharpest frames, ensuring they are not 
    from the same time interval.
    """
    if not os.path.exists(video_path):
        print(f"Error: Video file {video_path} not found.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if fps == 0:
        print("Error: Could not read video properties.")
        return

    print(f"Processing video: {video_path}")
    print(f"Total frames: {total_frames}, FPS: {fps:.2f}")

    frames_data = []
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        timestamp = frame_count / fps
        sharpness = calculate_sharpness(frame)
        frames_data.append({
            'frame_index': frame_count,
            'timestamp': timestamp,
            'sharpness': sharpness,
            'frame': frame.copy() if frame_count % 10 == 0 else None # Memory optimization: don't store all frames
        })
        
        frame_count += 1
        if frame_count % 100 == 0:
            print(f"Analyzed {frame_count}/{total_frames} frames...")

    # Sort frames by sharpness descending
    frames_data.sort(key=lambda x: x['sharpness'], reverse=True)

    selected_frames = []
    
    # Re-read video to get high-quality frames for the top candidates
    # This is more memory efficient than storing all frames in RAM
    for candidate in frames_data:
        if len(selected_frames) >= top_n:
            break
            
        # Check if this frame is far enough from already selected frames
        is_diverse = True
        for selected in selected_frames:
            if abs(candidate['timestamp'] - selected['timestamp']) < min_interval_sec:
                is_diverse = False
                break
        
        if is_diverse:
            # Extract the actual frame content
            cap.set(cv2.CAP_PROP_POS_FRAMES, candidate['frame_index'])
            ret, frame = cap.read()
            if ret:
                candidate['frame'] = frame
                selected_frames.append(candidate)
                print(f"Selected frame at {candidate['timestamp']:.2f}s (Sharpness: {candidate['sharpness']:.2f})")

    cap.release()

    # Save selected frames
    for i, data in enumerate(selected_frames):
        filename = f"sharp_frame_{i+1}_time_{data['timestamp']:.2f}s.jpg"
        filepath = os.path.join(output_dir, filename)
        cv2.imwrite(filepath, data['frame'])
        print(f"Saved: {filepath}")

    print("\nProcessing complete!")

#it help my use the progrem to use again as a libarary 
if __name__ == "__main__":
   
    video_path = r"photos.mp4"
    output_folder = r"output"
    
    #run program 
    process_video(video_path, output_folder, 5, 1.0)
