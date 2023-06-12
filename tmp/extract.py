import cv2

# Set the path to the video file
video_path = 'discord_conversations.mp4'

# Open the video file
video = cv2.VideoCapture(video_path)

# Initialize a counter to keep track of the frame number
frame_count = 0

# Read frames from the video
while True:
    # Read the next frame
    ret, frame = video.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Perform image processing or analysis on the frame here
    # For example, you can save the frame as an image file
    frame_filename = f'frame_{frame_count}.png'
    cv2.imwrite(frame_filename, frame)

    # Increment the frame counter
    frame_count += 1

# Release the video file
video.release()
