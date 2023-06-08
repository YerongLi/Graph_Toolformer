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
                speaker = "[Musk]"
            else:
                speaker = "[User]"

            formatted_lines.append(f"{speaker} {line} [{speaker} ({timestamp})]")
        else:
            formatted_lines.append(line)

# Save the cleaned content to a new file
with open("clean_03.txt", "w") as file:
    file.write("\n".join(formatted_lines))
