def reformat_conversation(file_path):
    conversation = ""
    speaker = "Host"

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith("WATTENBERG:"):
                speaker = "Host"
            elif line.startswith("MUSK:"):
                speaker = "Musk"
            elif line.strip() == "":
                continue
            else:
                line = f"[{speaker}] {line}"
                conversation += line

    return conversation

# Reformat the conversation in 1.txt
formatted_conversation = reformat_conversation("1.txt")
print(formatted_conversation)
