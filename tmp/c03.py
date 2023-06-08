import re

# Read the input file
with open("03.txt", "r") as file:
    content = file.readlines()

# Regular expression pattern for matching timestamps
timestamp_pattern = r"\((\d{2}:\d{2}:\d{2})\):"

# Clean and format the lines
formatted_lines = []
current_speaker = None
current_line = ""
for i, line in enumerate(content):
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
        line = re.sub(r"(\(.*?\))", "", line).strip().encode("ascii", "ignore").decode()
        real_speaker = line[:timestamp_match.start()].strip()
        # Extract the speaker from the line
        if current_speaker is None:
            current_speaker = real_speaker
        if "Elon Musk" in line:
            speaker = "[Musk]"
        else:
            speaker = "[User]"
        # print(real_speaker)
        if current_speaker is not None and current_speaker != real_speaker:
            formatted_lines.append(current_line.strip())
            current_line = f'{speaker} '
            current_speaker = real_speaker
        else:
            current_line += line
    else:
        current_line += line
    # if i > 30: break
if current_line:
    formatted_lines.append(current_line.strip())

# Save the cleaned content to a new file
with open("clean_03.txt", "w") as file:
    file.write("\n".join(formatted_lines))
