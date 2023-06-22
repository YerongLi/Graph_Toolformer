import glob

def has_non_tokenizable_characters(file_path):
    non_tokenizable_characters = ["\u2018", "\u00A0", "\u201C", "\u201C"]  # List of non-tokenizable characters

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        for character in non_tokenizable_characters:
            if character in content:
                return True

    return False


# Get a list of file paths matching the pattern "clean_*.txt"
file_paths = glob.glob("clean_*.txt")

# Iterate over the file paths and check for non-tokenizable characters
for file_path in file_paths:
    if has_non_tokenizable_characters(file_path):
        print(f"File '{file_path}' contains non-tokenizable characters.")
    else:
        print(f"File '{file_path}' does not contain non-tokenizable characters.")
