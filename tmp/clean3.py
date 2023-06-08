import re

# Read the input file
with open("03.txt", "r") as file:
    content = file.read()

# Split the content into lines
lines = content.splitlines()

# Regular expression patterns for matching timestamps and speakers
timestamp_pattern = r"\((\d{2}:\d{2}:\d{2})\):"
speaker_pattern = r"^(.*?)(?: \(\d{2}:\d{2}:\d{2}\))?:"

# Clean and format the lines
formatted_lines = []
for line in lines:
    # Remove leading/trailing whitespaces
    line = line.strip()
    
    # Match the timestamp
    timestamp_match = re.search(timestamp_pattern, line)
    if timestamp_match:
        timestamp = timestamp_match.group(1)
        line = line.replace(timestamp_match.group(0), "")
        
        # Match the speaker
        speaker_match = re.search(speaker_pattern, line)
        if speaker_match:
            speaker = speaker_match.group(1)
            if speaker == "Elon Musk":
                speaker = "Musk"
            else:
                speaker = "[User]"
                
            # Format the line
            line = f"{speaker} ({timestamp}): {line}"
    
    formatted_lines.append(line)

# Save the cleaned content to a new file
with open("clean_03.txt", "w") as file:
    file.write("\n".join(formatted_lines))
