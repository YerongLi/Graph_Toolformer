import re

# Read the input file
with open("03.txt", "r") as file:
    content = file.readlines()

# Regular expression pattern for matching timestamps
timestamp_pattern = r"\((\d{2}:\d{2}:\d{2})\):"

# Clean and format the lines
formatted_lines = []
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

        # Extract the speaker from the line
        if "Elon Musk" in line:
            speaker = "[Musk]"
        else:
            speaker = "[User]"

        formatted_line = f"{speaker}"
        formatted_lines.append(formatted_line)
    else:
        formatted_lines.append(line)

# Save the cleaned content to a new file
with open("clean_03.txt", "w") as file:
    file.write("\n".join(formatted_lines))
