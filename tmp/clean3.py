import re

# Read the input file
with open("03.txt", "r") as file:
    content = file.readlines()

# Regular expression pattern for matching speaker lines
line_pattern = r"^\[(.*?)\]\s*(.*)$"

# Clean and format the lines
formatted_lines = []
previous_speaker = None
for line in content:
    # Remove leading/trailing whitespaces
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    # Match the speaker line
    line_match = re.match(line_pattern, line)
    if line_match:
        speaker = line_match.group(1)
        utterance = line_match.group(2)

        # Format the line with speaker and utterance
        formatted_line = f"[{speaker}] {utterance}"

        # Append the line to the previous speaker's utterance if it's the same speaker
        if speaker == previous_speaker:
            formatted_lines[-1] += f" {utterance}"
        else:
            formatted_lines.append(formatted_line)
            previous_speaker = speaker

# Save the cleaned content to a new file
with open("clean_03.txt", "w") as file:
    file.write("\n".join(formatted_lines))
