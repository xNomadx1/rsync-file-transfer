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
## Rsync Options
```bash
	"-avh", 
        # -a: archive mode; recursively transfers directories and preserves metadata.
        # -v: displays transfer details.
        # -h: displays human-readable file sizes.
	"--partial",
        # Keeps an incomplete destination file if the transfer is interrupted, allowing a later transfer
        # to reuse it.
	"--append-verify",
        # Continues transferring from the end of an existing partial file, then verifies the completed
        # file. This is mainly useful for large interrupted transfers.
	"--info=progress2",
        # Displays progress for the entire transfer rather than only individual files.
	"--stats",
        # Prints a transfer summary, including file counts, bytes transferred, and speed.
	"--exclude=.DS_Store",
        # Skips .DS_Store metadata files created by macOS.
	"--exclude=Thumbs.db"
        # Skips Thumbs.db thumbnail files created by Windows.
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
