from huggingface_hub import snapshot_download

# Set your Hugging Face API token
hf_token = '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'

# Set repository information
repo_id = "meta-llama/Llama-2-70b-hf"
local_folder = "/scratch/yerong/.cache/pyllama/Llama-2-70b-hf"

# Download the snapshot
snapshot_download(
    repo_id=repo_id,
    local_dir=local_folder,
    use_auth_token=hf_token,
    local_dir_use_symlinks=False
)

print("Download complete.")

