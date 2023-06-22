import glob
import re

def has_non_tokenizable_characters(file_path):
    non_tokenizable_characters = ["\u2018", "\u00A0", "\u201C", "\u201C"]  # List of non-tokenizable characters
    invalid_characters = {}

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", content)  # Split content into sentences

        for character in non_tokenizable_characters:
            if character in content:
                for sentence in sentences:
                    if character in sentence:
                        invalid_characters[character] = sentence
                        break

    return invalid_characters


# Get a list of file paths matching the pattern "clean_*.txt"
file_paths = glob.glob("clean_*.txt")

# Iterate over the file paths and check for non-tokenizable characters
for file_path in file_paths:
    invalid_chars = has_non_tokenizable_characters(file_path)
    if invalid_chars:
        print(f"File '{file_path}' contains the following invalid characters:")
        for char, sentence in invalid_chars.items():
            unicode_code = ord(char)
            print(f"Invalid character: {char} (Unicode: U+{unicode_code:04X})")
            print(f"First sentence: {sentence}\n")
    else:
        print(f"File '{file_path}' does not contain invalid characters.")
