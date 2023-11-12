from gendiff.gendiff_pac import generate_diff, generate_diff_dic
from gendiff.gendiff_pac import get_files, format_diff_to_lst


path1 = 'tests/fixtures/file1.json'
path2 = 'tests/fixtures/file2.json'
path3 = 'tests/fixtures/file3.yml'
path4 = 'tests/fixtures/file4.yaml'

file1, file2 = get_files(path1, path2)
file3, file4 = get_files(path3, path4)
diff_dic_json = generate_diff_dic(file1, file2)
diff_dic_yml = generate_diff_dic(file3, file4)


def test_generate_diff_dic():
    assert generate_diff_dic(file1, file2) == {
        'host': {'file_key_val': 'hexlet.io', 'meta': 'match'},
        'timeout': {'file_key_val': (50, 20), 'meta': 'modified'},
        'proxy': {'file_key_val': '123.234.53.22', 'meta': '-'},
        'follow': {'file_key_val': False, 'meta': '-'},
        'verbose': {'file_key_val': True, 'meta': '+'}}

    assert generate_diff_dic(file3, file4) == {
        'host': {'file_key_val': 'hexlet.io', 'meta': 'match'},
        'timeout': {'file_key_val': (50, 20), 'meta': 'modified'},
        'proxy': {'file_key_val': '123.234.53.22', 'meta': '-'},
        'follow': {'file_key_val': False, 'meta': '-'},
        'verbose': {'file_key_val': True, 'meta': '+'}}


def test_format_diff_to_lst():
    assert format_diff_to_lst(diff_dic_json) == [
        "- {'follow': false}",
        "  {'host': 'hexlet.io'}",
        "- {'proxy': '123.234.53.22'}",
        "- {'timeout': 50}\n+ {'timeout': 20}",
        "+ {'verbose': True}"]

    assert format_diff_to_lst(diff_dic_yml) == [
        "- {'follow': false}",
        "  {'host': 'hexlet.io'}",
        "- {'proxy': '123.234.53.22'}",
        "- {'timeout': 50}\n+ {'timeout': 20}",
        "+ {'verbose': True}"]


def test_generate_diff():
    print(generate_diff(path1, path2))
    assert generate_diff(path1, path2) == """{\n- {'follow': false}\n  {'host': 'hexlet.io'}\n- {'proxy': '123.234.53.22'}\n- {'timeout': 50}\n+ {'timeout': 20}\n+ {'verbose': True}\n}"""

    print(generate_diff(path3, path4))
    assert generate_diff(path3, path4) == """{\n- {'follow': false}\n  {'host': 'hexlet.io'}\n- {'proxy': '123.234.53.22'}\n- {'timeout': 50}\n+ {'timeout': 20}\n+ {'verbose': True}\n}"""
