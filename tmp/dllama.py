import subprocess
import os
import time
import argparse
from datetime import datetime, timedelta

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def run_llama_download(model_size, folder):
    command = [
        "python", "-m", "llama.download",
        "--model_size", f"{model_size}B",
        "--folder", folder
    ]
    return subprocess.Popen(command)

def main(model_size):
    folder = "."  # Default folder is the current directory
    previous_process = None
    previous_start_time = None

    while True:
        if previous_process:
            print("Terminating previous download...")
            previous_process.terminate()
            previous_process.wait()

        print(f"Starting new download for model size {model_size}B...")
        current_process = run_llama_download(model_size, folder)
        previous_start_time = datetime.now()

        initial_size = get_folder_size(folder)
        while current_process.poll() is None:  # While the process is running
            time.sleep(120)  # Wait for 120 seconds
            current_size = get_folder_size(folder)
            if current_size <= initial_size:
                elapsed_time = datetime.now() - previous_start_time
                if elapsed_time > timedelta(seconds=120):
                    print("Folder size did not increase for 120 seconds, terminating and restarting download...")
                    current_process.terminate()
                    current_process.wait()
                    current_process = run_llama_download(model_size, folder)
                    previous_start_time = datetime.now()
                else:
                    print("Folder size did not increase, continuing...")
            else:
                print("Folder size increased, continuing...")
                initial_size = current_size

        previous_process = current_process

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download LLAMA model and monitor folder size.")
    parser.add_argument("model_size", type=int, choices=[7, 13, 30, 65], help="Model size (7, 13, 30, or 65).")

    args = parser.parse_args()
    main(args.model_size)

