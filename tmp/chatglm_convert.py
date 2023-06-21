import json

# Open the input file
with open("clean_01.txt", "r") as file:
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

# Save the data to a JSON file
with open("elon_musk.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
