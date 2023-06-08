import re

# Read the input file
with open("05.txt", "r") as file:
    content = file.readlines()

# Regular expression pattern for matching timestamps
timestamp_pattern = r"\[(\d{2}:\d{2}:\d{2})\]"

# Clean and format the lines
formatted_lines = []
current_speaker = None
current_line = ""
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
        line = re.sub(r"(\[.*?\])", "", line).strip()
        real_speaker = line[:line.index(":")].strip()
        # Extract the speaker from the line
        if current_speaker is None:
            current_speaker = real_speaker
        if "Elon Musk" in line:
            speaker = "[Musk]"
        else:
            speaker = "[User]"
        if current_speaker is not None and current_speaker != real_speaker:
            formatted_lines.append(current_line.strip())
            current_line = f'{speaker} {line[line.index(":") + 1:].strip()}'
            current_speaker = real_speaker
        else:
            current_line += f' {line[line.index(":") + 1:].strip()}'
    else:
        current_line += f' {line.strip()}'

if current_line:
    formatted_lines.append(current_line.strip())

# Save the cleaned content to a new file
with open("clean.05.txt", "w") as file:
    file.write("\n".join(formatted_lines))
