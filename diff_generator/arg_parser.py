from argparse import ArgumentParser

def validate_file_ext(file1, file2):
    valid_extensions = (".json", ".yaml", ".yml")
    if not file1 or not file2:
        raise ValueError("Invalid file paths")
    if not (file1.lower().endswith(valid_extensions) and 
            file2.lower().endswith(valid_extensions)):
        raise ValueError("Allowed extensions: .json, .yaml, .yml")
    return True

def parse_input():
    parser = ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument('-f', '--format', type=str, default="stylish", help="set format of output")
    return parser.parse_args()

def main():
    args = parse_input()
    validate_file_ext(args.first_file, args.second_file)
    print(f"Comparing: {args.first_file} vs {args.second_file}")

if __name__ == "__main__":
    main()