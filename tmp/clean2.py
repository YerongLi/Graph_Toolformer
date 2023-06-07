import re

# Read the conversation from the file
with open("02.txt", "r") as file:
    conversation = file.read()

# Remove unnecessary tags
conversation = re.sub(r'\[(Host|Musk)\]', '', conversation)

# Clean up the conversation text
conversation = conversation.strip()

# Replace names with tags
conversation = re.sub(r'Peter Campbell \(PC\):', '[Host]:', conversation)
conversation = re.sub(r'Elon Musk \(EM\):', '[Musk]:', conversation)
conversation = re.sub(r'PC:', '[Host]:', conversation)
conversation = re.sub(r'EM:', 'Musk:', conversation)


# Remove extra spaces and newlines
conversation = re.sub(r'\n+', '\n', conversation)
conversation = re.sub(r' +', ' ', conversation)

# Print the cleaned up conversation
print(conversation)
