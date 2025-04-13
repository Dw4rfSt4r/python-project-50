from diff_generator.arg_parser import validate_file_ext
import pytest # type: ignore


def test_valid_extensions():
    assert validate_file_ext("file.json", "file.yaml") is True

def test_invalid_extension():
    with pytest.raises(ValueError):
        validate_file_ext("file.txt", "file.yaml")

def test_empty_file1():
    with pytest.raises(ValueError):
        validate_file_ext("", "file.yaml")

def test_empty_file2():
    with pytest.raises(ValueError):
        validate_file_ext("file.json", "")
