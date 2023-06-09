import json

# Path to the JSON file
json_file = "OpenEnded_mscoco_train2014_questions.json"

# Path to the output file
output_file = "questions.txt"

# Function to parse the JSON file and extract questions
def parse_json(file_path, output_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    questions = data["questions"]  # Extract first 100 questions

    with open(output_path, "w") as f:
        for question in questions:
            question_text = question["question"]
            f.write(question_text + "\n")  # Write each question on a new line

    print("Questions have been saved to", output_path)

# Call the function to parse the JSON file and save questions
parse_json(json_file, output_file)
