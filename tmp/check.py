import glob

def has_non_tokenizable_characters(file_path):
    non_tokenizable_characters = ["\u2018", "\u00A0", "\u201C", "\u201C"]  # List of non-tokenizable characters
    invalid_characters = []

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        for character in non_tokenizable_characters:
            if character in content:
                invalid_characters.append(character)

    return invalid_characters


# Get a list of file paths matching the pattern "clean_*.txt"
file_paths = glob.glob("clean_*.txt")

# Iterate over the file paths and check for non-tokenizable characters
for file_path in file_paths:
    invalid_chars = has_non_tokenizable_characters(file_path)
    if invalid_chars:
        print(f"File '{file_path}' contains the following invalid characters:")
        for char in invalid_chars:
            unicode_code = ord(char)
            print(f"Invalid character: {char} (Unicode: U+{unicode_code:04X})")
    else:
        print(f"File '{file_path}' does not contain invalid characters.")
