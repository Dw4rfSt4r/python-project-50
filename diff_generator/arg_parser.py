import json
from argparse import ArgumentParser

import yaml


def validate_file_ext(file1, file2):
    valid_extensions = (".json", ".yaml", ".yml")
    if not file1 or not file2:
        raise ValueError("Invalid file paths")
    if not (file1.lower().endswith(valid_extensions) and 
            file2.lower().endswith(valid_extensions)):
        raise ValueError("Allowed extensions: .json, .yaml, .yml")
    return True


def get_filepath():
    parser = ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        '-f', '--format',
        type=str,
        default="stylish",
        choices=["stylish", "plain"],
        help="set format of output")
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def read_file(file_path):
    with open(file_path) as file:
        if file_path.endswith(".json"):
            return json.load(file)
        if file_path.endswith(".yaml") or file_path.endswith(".yml"):
            return yaml.safe_load(file)
