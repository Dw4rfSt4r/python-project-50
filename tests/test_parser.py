import pytest  # type: ignore

from gendiff.arg_parser import validate_file_ext


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


def test_case_sensitivity():
    assert validate_file_ext("file.JSON", "file.YAML") is True
    assert validate_file_ext("file.Json", "file.Yml") is True


def test_only_extension():
    with pytest.raises(ValueError):
        validate_file_ext(".json", "file.yaml")
        
    with pytest.raises(ValueError):
        validate_file_ext("file.json", ".yaml")