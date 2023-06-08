import re


import re

# Line pattern for matching timestamps and speaker names
line_pattern = r"\[\s*(\d{2}:\d{2}:\d{2})\s*\]\s*(\w+)\s*"

# Example lines
lines = [
    "[00:19:26] Joe Rogan",
    "[00:19:27] Elon Musk",
    "This line doesn't match the pattern",
]

for line in lines:
    # Check if the line matches the pattern
    line_match = re.match(line_pattern, line)
    if line_match:
        print(f"Line matches the pattern: {line}")
    else:
        print(f"Line does not match the pattern: {line}")

# Read the input file
with open("05.txt", "r") as file:
    content = file.readlines()

# Regular expression pattern for matching timestamps and speaker names
line_pattern = r"\[\s*(\d{2}:\d{2}:\d{2})\s*\]\s*(\w+)\s*"


# Clean and format the lines
formatted_lines = []
current_speaker = None
current_line = ""
for i, line in enumerate(content):
    # Remove leading/trailing whitespaces
    line = line.strip()
    print(line)
    # Skip empty lines
    if not line:
        continue

    # Match the line pattern
    line_match = re.match(line_pattern, line)
    print(line_match)

    if line_match:
        timestamp = line_match.group(1)
        speaker = line_match.group(2)
        line = re.sub(line_pattern, "", line).strip()

        # Extract the real_speaker from the line
        real_speaker_match = re.match(r"\b([A-Za-z\s]+)\b", line)
        if real_speaker_match:
            real_speaker = real_speaker_match.group(1).strip()
        else:
            real_speaker = ""

        # Set the current_speaker if not already set
        if current_speaker is None:
            current_speaker = real_speaker

        # Determine the speaker tag
        if speaker == "Elon Musk":
            speaker_tag = "[Musk]"
        else:
            speaker_tag = "[User]"

        # Check if the speaker has changed
        if current_speaker != real_speaker:
            formatted_lines.append(current_line.strip())
            current_line = f'{speaker_tag} {line}'
            current_speaker = real_speaker
        else:
            current_line += f' {line}'
    else:
        current_line += f' {line}'
    if i > 5: break

    # Print if the timestamp regex matches
    if line_match:
        print("Timestamp Match:", line_match.groups())

if current_line:
    formatted_lines.append(current_line.strip())

# Save the cleaned content to a new file
with open("clean_05.txt", "w") as file:
    file.write("\n".join(formatted_lines))
