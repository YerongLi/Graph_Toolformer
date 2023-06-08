import re

# Read the input file
with open("03.txt", "r") as file:
    content = file.readlines()

# Regular expression patterns for matching timestamps and speakers
timestamp_pattern = r"\((\d{2}:\d{2}:\d{2})\):"
speaker_pattern = r"^(.*?)(?: \(\d{2}:\d{2}:\d{2}\))?:"

# Clean and format the lines
formatted_lines = []
current_speaker = None
current_utterance = ""
for line in content:
    # Remove leading/trailing whitespaces
    line = line.strip()
    
    # Skip empty lines
    if not line:
        continue
    
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
                
            # Start a new utterance if the speaker changes
            if current_speaker != speaker:
                if current_speaker:
                    formatted_lines.append(current_utterance.strip())
                current_speaker = speaker
                current_utterance = f"{current_speaker} ({timestamp}): {line}"
            else:
                current_utterance += f" {line}"
    
    formatted_lines.append(current_utterance.strip())

# Save the cleaned content to a new file
with open("clean_03.txt", "w") as file:
    file.write("\n".join(formatted_lines))
