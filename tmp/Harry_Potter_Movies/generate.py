import pandas as pd

# Define the file paths
dialogue_file = 'Dialogue.csv'
character_file = 'Characters.csv'

# Load character map
character_map = {}
character_df = pd.read_csv(character_file, encoding='unicode_escape')

for index, row in character_df.iterrows():
    character_id = row['Character ID']
    character_name = row['Character Name']
    character_map[character_id] = character_name

# Read dialogue file
dialogue_df = pd.read_csv(dialogue_file, encoding='unicode_escape')

# Sort dialogue dataframe by Chapter ID and Place ID
dialogue_df = dialogue_df.sort_values(by=['Chapter ID', 'Place ID'])

# Counter for file names
file_counter = 1

# Variables to track the previous Chapter ID and Place ID
previous_chapter_id = None
previous_place_id = None

# Iterate over the dialogue rows
for index, row in dialogue_df.iterrows():
    chapter_id = row['Chapter ID']
    place_id = row['Place ID']
    dialogue = row['Dialogue']
    character_id = row['Character ID']
    character_name = character_map.get(character_id)

    # Check if Chapter ID or Place ID changed
    if chapter_id != previous_chapter_id or place_id != previous_place_id:
        output_file = f'clean_{file_counter:03d}.txt'
        file_counter += 1
        previous_chapter_id = chapter_id
        previous_place_id = place_id

    # Write dialogue to the current output file
    with open(output_file, 'a') as file:
        if character_name:
            file.write(f'[{character_name}] {dialogue}\n')
