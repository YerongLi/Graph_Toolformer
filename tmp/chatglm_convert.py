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
data = {
    "instruction": "",
    "output": "",
    "history": []
}
history_start_idx = max(0, len(conversation) - 10)
for i in range(history_start_idx, len(conversation) - 1):
    data["history"].append(conversation[i]["utterance"])

for i in range(len(conversation) - 1):
    if conversation[i]["role"] == "Human":
        data["instruction"] += f"{conversation[i]['role']}:{conversation[i]['utterance']}\n"
        data["output"] += f"{conversation[i+1]['role']}:{conversation[i+1]['utterance']}\n"

# Save the data to a JSON file
with open("elon_musk.json", "w") as json_file:
    json.dump(data, json_file, indent=4)