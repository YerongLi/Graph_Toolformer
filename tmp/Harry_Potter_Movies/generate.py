import pandas as pd

# Define the file paths
dialogue_file = 'Dialogue.csv'
character_file = 'Characters.csv'
output_file = 'dialogue.txt'

# Load character map
character_map = {}
character_df = pd.read_csv(character_file, encoding='unicode_escape')

for index, row in character_df.iterrows():
    character_id = row['Character ID']
    character_name = row['Character Name']
    character_map[character_id] = character_name

# Read dialogue file in order
dialogue_df = pd.read_csv(dialogue_file, encoding='unicode_escape')

# Write dialogue to the output file
with open(output_file, 'w') as file:
    for index, row in dialogue_df.iterrows():
        character_id = row['Character ID']
        dialogue = row['Dialogue']
        character_name = character_map.get(character_id)
        if character_name:
            file.write(f'[{character_name}] {dialogue}\n')
