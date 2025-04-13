from diff_generator.arg_parser import parse_input, validate_file_ext


def main():
    args = parse_input()
    validate_file_ext(args.first_file, args.second_file)
    return

if __name__ == "__main__":
    main()
