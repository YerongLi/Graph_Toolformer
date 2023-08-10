import subprocess

def run_llama_command(input_string):
    # Define the command as a list of individual components
    command = [
        "$SCRATCH/llama.cpp/main",
        "-m",
        "$SCRATCH/.cache/pyllama/7B/ggml-model-q4_0.bin",
        "-p",
        f'"{input_string}"',  # Wrap input_string with double quotes
        "-t",
        "1",
        "-n",
        "128",
        "--temp",
        "0.1",
        "--top-p",
        "0.90",
        "-ngl",
        "83"
    ]

    # Join the command list into a single string with spaces
    command_str = " ".join(command)

    try:
        result = subprocess.run(command_str, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing the command: {e}"

# Example usage
input_string = "Who is Elon Musk ?"
output = run_llama_command(input_string)
print("output")
print(output)
