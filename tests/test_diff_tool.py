from diff_generator.arg_parser import read_file
from diff_generator.diff_tool import process_flat_files

json1 = read_file("tests/test_data/flat_1.json")

json2 = read_file("tests/test_data/flat_2.json")

yml1 = read_file("tests/test_data/flat_1.yml")

yml2 = read_file("tests/test_data/flat_2.yaml")



def test_process_flat_files():
    expected = {
        "host": {
            "status": "unchanged",
            "value": "hexlet.io"},
        "timeout": {
            "status": "changed", 
            "old_value": 50, 
            "new_value": 20},
        "proxy": {
            "status": "removed", 
            "value": "123.234.53.22"},
        "follow": {
            "status": "removed",
            "value": False},
        "verbose": {
            "status": "added",
            "value": True}
    }
    assert process_flat_files(json1, json2) == expected
    assert process_flat_files(yml1, yml2) == expected
    assert process_flat_files(json1, yml2) == expected
