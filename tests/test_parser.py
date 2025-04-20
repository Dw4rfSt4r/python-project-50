import pytest  # type: ignore

from diff_generator.arg_parser import validate_file_ext


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


"""# Тесты с путями до файлов
def test_read_json_file1():
    path1 = 'tests/fixtures/plane_json_1.json'
    expected_data = {"key1": "value1"}
    
    # Читаем файл и проверяем его содержимое
    result = read_file(path1)
    assert result == expected_data  # Ожидаемое содержимое

def test_read_json_file2():
    path2 = 'tests/fixtures/plane_json_2.json'
    expected_data = {"key2": "value2"}"""