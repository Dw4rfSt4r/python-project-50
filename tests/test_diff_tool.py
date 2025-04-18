from diff_generator.diff_tool import process_flat_files
from diff_generator.arg_parser import read_file

file1 = read_file("tests/fixtures/flat_1.json")
'''
{
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": false
}
'''
file2 = read_file("tests/fixtures/flat_2.json")
'''
{
    "timeout": 20,
    "verbose": true,
    "host": "hexlet.io"
}
'''
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
    assert process_flat_files(file1, file2) == expected
