import cv2
import numpy as np
import os
from tqdm import tqdm

# Set the path to the video file
video_path = 'discord_conversations.mp4'
output_folder = 'frames'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the video file
video = cv2.VideoCapture(video_path)

# Initialize variables
prev_frame = None
frame_count = 0

# Get total number of frames in the video
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Create tqdm progress bar
progress_bar = tqdm(total=total_frames, unit='frames', desc='Processing Frames')

# Read frames from the video
while True:
    # Read the next frame
    ret, frame = video.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to the grayscale frame
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Dilate the thresholded frame to enhance the differences
    dilated = cv2.dilate(thresh, None, iterations=2)

    # Check if there is a previous frame
    if prev_frame is not None:
        # Compute the absolute difference between the current and previous frames
        diff = cv2.absdiff(dilated, prev_frame)

        # Count the number of non-zero pixels in the difference image
        diff_count = np.count_nonzero(diff)

        # Save the frame only if it has significant differences from the previous frame
        if diff_count > 1000:
            frame_filename = os.path.join(output_folder, f'frame_{frame_count}.png')
            cv2.imwrite(frame_filename, frame)
            frame_count += 1

    # Update the previous frame with the current frame
    prev_frame = dilated

    # Update progress bar
    progress_bar.update(1)

# Release the video file
video.release()

# Close the progress bar
progress_bar.close()
