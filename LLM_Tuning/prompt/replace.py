def process_prompt_file(filename="knowledge_graphs/freebase/prompts_train", output_filename="knowledge_graphs/conceptnet/prompts_train"):
    # Read input from file
    with open(filename, "r") as file:
        input_text = file.read()

    # Perform string replacements
    output_text = input_text.replace("According to the Freebase knowledge graph,", "According to the Concept knowledge graph,")
    output_text = output_text.replace('GL("Freebase")', 'GL("Concept")')
    output_text = input_text.replace("[", "<yerongAPI>")
    output_text = output_text.replace("]", "</yerongAPI>")

    # Create the output filename

    # Write the output to a new file
    with open(output_filename, "w") as file:
        file.write(output_text)

    # Return the output filename
    return output_filename

# Example usage
output_filename = process_prompt_file()
print(f"Output saved to: {output_filename}")