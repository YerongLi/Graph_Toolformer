import re

# Read the input file
with open("03.txt", "r") as file:
    content = file.readlines()

# Regular expression pattern for matching timestamps
timestamp_pattern = r"\((\d{2}:\d{2}:\d{2})\):"

# Clean and format the lines
formatted_lines = []
current_speaker = '[User] '
current_line = "[User] "
for i, line in enumerate(content):
    # print('before')
    # print(line)
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
        line = line.replace("<E2><80><99>", "'")
        # Extract the speaker from the line
        if "Elon Musk" in line:
            speaker = "[Musk] "
        else:
            speaker = "[User] "
        if current_speaker is not None and current_speaker != speaker:
            formatted_lines.append(current_line.strip())
            current_line = f'{speaker}'
            current_speaker = speaker
        else:
            current_line += line
    else:
        current_line += line
    # print('after', current_line)
    # if i > 30: break
if current_line:
    formatted_lines.append(current_line.strip())

# Save the cleaned content to a new file
with open("clean_03.txt", "w") as file:
    file.write("\n".join(formatted_lines))
