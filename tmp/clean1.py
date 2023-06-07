import re

def reformat_conversation(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        line = line.strip()
        match = re.match(r'^(WATTENBERG|MUSK):', line)
        if match:
            speaker = '[Host]' if match.group(1) == 'WATTENBERG' else '[Musk]'
            cleaned_lines.append(f'{speaker} {line[len(match.group(0)):]}')

    with open(output_file, 'w') as file:
        file.write('\n'.join(cleaned_lines))

# Specify the input and output file paths
input_file = '01.txt'
output_file = '01_clean.txt'

# Reformat the conversation
reformat_conversation(input_file, output_file)
