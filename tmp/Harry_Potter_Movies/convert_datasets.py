from datetime import date
import json
import os

def extract_conversation(filename, name, json_filename):
    # Open the input file
    with open(filename, "r") as file:
        content = file.readlines()

    # Extract the conversation between the user and the specified name
    conversation = []
    for line in content:
        if f"[{name}]" in line:
            role = "Assistant"
        else:
            role = "Human"
        utterance = line.split("]", 1)[1].strip()
        conversation.append({"role": role, "utterance": utterance})

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
        with open(json_filename, "a") as f:
            json.dump(data, f)
            f.write("\n")

def extract_single_conversation(filename, name, json_filename):
    # Open the input file
    with open(filename, "r") as file:
        content = file.readlines()

    # Extract the conversation between the user and the specified name
    conversation = []
    for line in content:
        if f"[{name}]" in line:
            role = "Assistant"
        else:
            role = "Human"
        utterance = line.split("]", 1)[1].strip()
        conversation.append({"role": role, "utterance": utterance})

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
        with open(json_filename, "a") as f:
            json.dump(data, f)
            f.write("\n")

# Prompt the user to enter the name to replace
name = input("Enter the name to replace (Musk or Harry Potter): ")

# Define the JSON file name
json_filename = f"{name.lower().replace(' ', '_')}.json"

# Process "clean_" files
for filename in os.listdir():
    if filename.startswith("clean_") and filename.endswith(".txt"):
        # Open the file and extract the conversation data
        print(filename)
        extract_conversation(filename, name, json_filename)

# Process "single_turn.txt" if it exists
single_turn_filename = "single_turn.txt"
if os.path.exists(single_turn_filename):
    extract_single_conversation(single_turn_filename, name, json_filename)
