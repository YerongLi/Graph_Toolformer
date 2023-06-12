import cv2
import pytesseract

# Set the path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set the path to the video file
video_path = 'discord_conversations.mp4'

# Open the video file
video = cv2.VideoCapture(video_path)

# Define the text extraction function
def extract_text_from_frame(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform text extraction using OCR
    text = pytesseract.image_to_string(gray)

    # Remove leading/trailing whitespaces and newlines
    text = text.strip()

    return text

# Initialize variables to store unique extracted text
unique_text = set()

# Read frames from the video
while True:
    # Read the next frame
    ret, frame = video.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Extract text from the frame
    text = extract_text_from_frame(frame)

    # Add the extracted text to the set of unique text
    unique_text.add(text)

# Print the unique extracted text
for text in unique_text:
    print(text)

# Release the video file
video.release()

