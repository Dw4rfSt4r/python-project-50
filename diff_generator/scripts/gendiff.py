from diff_generator.arg_parser import get_filepath, validate_file_ext, read_file


def main():
    args = get_filepath()
    validate_file_ext(args.first_file, args.second_file)
    file_1 = read_file(args.first_file)
    file_2 = read_file(args.second_file)

    return

if __name__ == "__main__":
    main()
