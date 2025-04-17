from diff_generator.arg_parser import get_filepath, validate_file_ext, read_file
from diff_generator.diff_tool import process_flat_files
from diff_generator.formatter import format_stylish


def main():
    first_file, second_file = get_filepath()
    validate_file_ext(first_file, second_file)
    file_1 = read_file(first_file)
    file_2 = read_file(second_file)
    diff = process_flat_files(file_1, file_2)
    print(format_stylish(diff))
    return

if __name__ == "__main__":
    main()
