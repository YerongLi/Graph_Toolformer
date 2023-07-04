import csv

# Define the file paths
dialogue_file = 'Dialogue.csv'
character_file = 'Characters.csv'
output_file = 'dialogue.txt'

# Load character map
character_map = {}
with open(character_file, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        character_id = int(row['Character ID'])
        character_name = row['Character Name']
        character_map[character_id] = character_name

# Extract dialogue for all characters
character_dialogue = {}
with open(dialogue_file, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        character_id = int(row['Character ID'])
        dialogue = row['Dialogue']
        if character_id not in character_dialogue:
            character_dialogue[character_id] = []
        character_dialogue[character_id].append(dialogue)

# Write dialogue to the output file
with open(output_file, 'w') as file:
    for character_id, dialogues in character_dialogue.items():
        character_name = character_map.get(character_id)
        if character_name:
            for dialogue in dialogues:
                file.write(f'[{character_name}] {dialogue}\n')
