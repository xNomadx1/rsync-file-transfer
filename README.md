# Rsync File Transfer

A small Python CLI for sending files and directories to remote Linux and macOS
computers with `rsync` over SSH.

## Setup

Requires Python 3.11+, `rsync`, and SSH access to the target computer.

```bash
python3 -m venv .venv_transfer
source .venv_transfer/bin/activate
pip install -r requirements.txt
cp config.example.toml config.toml
```

Edit `config.toml` with your source folders and remote targets. Linux home
directories normally use `/home/username/`; macOS uses `/Users/username/`.

## Usage

```bash
python3 transfer.py SOURCE_KEY TARGET_KEY FILE_OR_DIRECTORY
```

Examples:

```bash
# Send one file
python3 transfer.py files mac_files "example.py"

# Send a directory
python3 transfer.py home mac_files "Bash-Scripts"

# Send multiple files
python3 transfer.py downloads linux_files "file-one.zip" "file-two.zip"
```
