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
start_idx = max(0, len(conversation) - 10)
for i in range(start_idx, len(conversation)):
    if conversation[i]["role"] == "Human":
        instruction = f"{conversation[i]['role']}:{conversation[i]['utterance']}"
    else:
        instruction += f"\n{conversation[i]['role']}:{conversation[i]['utterance']}"
    data.append({"instruction": instruction})

# Save the data to a JSON file
with open("elon_musk.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
