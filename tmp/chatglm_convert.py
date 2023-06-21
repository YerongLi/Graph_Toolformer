import json
import os

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
    data = []
    for i in range(len(conversation) - 1):
        history_start_idx = max(0, i - 10)
        history = [conv["utterance"] for conv in conversation[history_start_idx:i]]
        instruction = conversation[i]["utterance"]
        if conversation[i + 1]["role"] == "Human": continue
        output = conversation[i + 1]["utterance"]
        data.append({
            "instruction": instruction,
            "output": output,
            "history": history
        })
final_data = []

# Loop through all files in the current directory that start with "clean_" and end with ".txt"
for filename in os.listdir():
    if filename.startswith("clean_") and filename.endswith(".txt"):
        # Open the file and extract the conversation data
        with open(filename, "r") as f:
            conversation_data = extract_conversation(f.read())
        # Append the conversation data to the final data list
        final_data.append(conversation_data)

# Dump the final data list as a JSON file
with open("final_data.json", "w") as f:
    json.dump(final_data, f)