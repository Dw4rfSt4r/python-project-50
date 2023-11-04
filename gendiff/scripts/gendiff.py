from gendiff.gendiff_cli import get_filepaths
from gendiff.gendif import generate_diff


def main():
    path1, path2 = get_filepaths()
    print(generate_diff(path1, path2))


if __name__ == '__main__':
    main()
