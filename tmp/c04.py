import re

# Read the input file
with open("04.txt", "r") as file:
    text = file.read()

# Define regex patterns for matching and replacing text
patterns = [
    (r'FABER:', '\n[User]'),
    (r'MUSK:', '\n[Musk]'),
    (r'\n+', '\n'),
    (r' +', ' '),
]

# Apply regex patterns to clean the text
for pattern, replacement in patterns:
    text = re.sub(pattern, replacement, text)

# Save the cleaned text to a new file
with open("clean_04.txt", "w") as file:
    file.write(text)

print("Cleaning complete. File saved as 'clean_04.txt'.")
