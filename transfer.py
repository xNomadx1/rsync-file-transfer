#!/usr/bin/env python3

import argparse
import os
import subprocess
import tomllib
from pathlib import Path
from dotenv import load_dotenv


def load_config() -> dict:
    with open("config.toml", "rb") as file:
        return tomllib.load(file)


def expand_env(value: str) -> str:
    return os.path.expandvars(value)


def run_rsync(source: Path, targets: str, options: list[str]) -> None:
    if not source.exists():
        print(f"Skipping missing file: {source}")
        return

    command = [
        "rsync",
        *options,
        str(source),
        targets,
    ]

    print("Running:")
    print(" ".join(command))
    print()

    subprocess.run(command, check=True)


def main() -> None:
    load_dotenv()

    parser = argparse.ArgumentParser(description="Transfer files using rsync.")
    parser.add_argument("source_key")
    parser.add_argument("target_key")
    parser.add_argument("files", nargs="+")

    args = parser.parse_args()
    config = load_config()

    source_folder = Path(expand_env(config["source"][args.source_key])).expanduser()
    target_folder = expand_env(config["targets"][args.target_key])
    options = config["rsync"]["options"]

    for filename in args.files:
        run_rsync(source_folder / filename, target_folder, options)


if __name__ == "__main__":
    main()