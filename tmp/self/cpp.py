import subprocess

# Define the command as a list of individual components
command = [
    "$SCRATCH/llama.cpp/main",
    "-m",
    "$SCRATCH/.cache/pyllama/65B/ggml-model-q4_0.bin",
    "-p",
    "\"Who is Elon Musk\"",  # Double-quotes are included around the argument
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

# Run the command using subprocess
try:
    result = subprocess.run(command_str, shell=True, check=True, capture_output=True, text=True)
    # The output will be stored in the 'result.stdout' variable
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Error executing the command:", e)
