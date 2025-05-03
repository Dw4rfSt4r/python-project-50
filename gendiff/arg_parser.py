import json
from argparse import ArgumentParser

import yaml


def validate_file_ext(file1, file2) -> bool:
    """
    Validates the file extensions of the input files.
    Raises ValueError if the extensions are invalid.
    Args:
        file1 (str): The path to the first file.
        file2 (str): The path to the second file.
    Returns:
        bool: True if the extensions are valid, False otherwise.
    """
    valid_extensions = (".json", ".yaml", ".yml")
    if not file1 or not file2:
        raise ValueError("Invalid file paths")
    if not (file1.lower().endswith(valid_extensions) and 
            file2.lower().endswith(valid_extensions)):
        raise ValueError("Allowed extensions: .json, .yaml, .yml")
    if file1.startswith(".") or file2.startswith("."):
        raise ValueError("File paths cannot start with a dot")
    return True


def get_filepath() -> tuple:
    """
    Parses command-line arguments and returns the file paths and format.
    Returns:
        tuple: A tuple containing the file paths and format.
    """
    parser = ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        '-f', '--format',
        type=str,
        default="stylish",
        choices=["stylish", "plain", "json"],
        help="set format of output")
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def read_file(file_path) -> dict:
    """
    Reads a file and returns its contents as a dictionary.
    Args:
        file_path (str): The path to the file.
    Returns:
        dict: The contents of the file as a dictionary.
    """
    with open(file_path) as file:
        if file_path.endswith(".json"):
            return json.load(file)
        if file_path.endswith(".yaml") or file_path.endswith(".yml"):
            return yaml.safe_load(file)
