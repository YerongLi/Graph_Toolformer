from datetime import date
import json
import os
if os.path.exists("elon_musk.json"):
    os.remove("elon_musk.json")
def extract_conversation(filename):
    # Open the input file
    with open(filename, "r") as file:
        content = file.readlines()

    # Extract the conversation between the user and Elon Musk
    conversation = []
    for line in content:
        if "[User]" in line:
            conversation.append({"role": "Human", "utterance": line.replace("[User]", "").strip()})
        elif "[Musk]" in line:
            conversation.append({"role": "Assistant", "utterance": line.replace("[Musk]", "").strip()})

    # Prepare the data in JSON format
    data = {
        "instruction": None,
        "output": None,
        "history": []
    }
    for i in range(len(conversation) - 1):
        if not (conversation[i]["role"] == "Human" and conversation[i + 1]["role"] == "Assistant"):
            continue
        history_start_idx = max(0, i - 6)
        history = [conv["utterance"] for conv in conversation[history_start_idx:i]]
        if len(history) % 2 != 0:
            continue
        history = [[history[i], history[i + 1]] for i in range(0, len(history), 2) if i + 1 < len(history)]
        instruction = conversation[i]["utterance"]
        output = conversation[i + 1]["utterance"]
        data["instruction"] = instruction
        data["output"] = output
        data["history"] = history
        # Dump each conversation as a separate JSON object in the file
        with open("elon_musk.json", "a") as f:
            json.dump(data, f)
            f.write("\n")

def extract_single_conversation(filename):
    # Open the input file
    with open(filename, "r") as file:
        content = file.readlines()

    # Extract the conversation between the user and Elon Musk
    conversation = []
    for line in content:
        if "[User]" in line:
            conversation.append({"role": "Human", "utterance": line.replace("[User]", "").strip()})
        elif "[Musk]" in line:
            conversation.append({"role": "Assistant", "utterance": line.replace("[Musk]", "").strip()})

    # Prepare the data in JSON format
    data = {
        "instruction": None,
        "output": None,
        "history": []
    }
    for i in range(len(conversation) - 1):
        if not (conversation[i]["role"] == "Human" and conversation[i + 1]["role"] == "Assistant"):
            continue
        instruction = conversation[i]["utterance"]
        output = conversation[i + 1]["utterance"]
        data["instruction"] = instruction
        data["output"] = output
        # Dump each conversation as a separate JSON object in the file
        with open("elon_musk.json", "a") as f:
            json.dump(data, f)
            f.write("\n")

# Loop through all files in the current directory that start with "clean_" and end with ".txt"
for filename in os.listdir():
    if filename.startswith("clean_") and filename.endswith(".txt"):
        # Open the file and extract the conversation data
        print(filename)
        extract_conversation(filename)
extract_single_conversation('chaoran_with_musk.txt')
