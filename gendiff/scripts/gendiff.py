from gendiff.arg_parser import get_filepath, read_file, validate_file_ext
from gendiff.diff_tool import generate_diff


def main():
    first_file, second_file, format_name = get_filepath()
    validate_file_ext(first_file, second_file)
    file_1 = read_file(first_file)
    file_2 = read_file(second_file)
    diff = generate_diff(file_1, file_2, format_name)
    print(diff)
    return


if __name__ == "__main__":
    main()
