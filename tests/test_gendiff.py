from gendiff.gendif import generate_diff, generate_diff_dic, build_diff_lst
from gendiff.gendif import get_files


path1 = '/home/snake/python-project-50/tests/file1.json'
path2 = '/home/snake/python-project-50/tests/file2.json'
file1, file2 = get_files(path1, path2)
diff_dic = generate_diff_dic(file1, file2)


assert generate_diff_dic(file1, file2) == {
    'host': {'file_key_val': 'hexlet.io', 'meta': 'match'},
    'timeout': {'file_key_val': (50, 20), 'meta': 'modified'},
    'proxy': {'file_key_val': '123.234.53.22', 'meta': '-'},
    'follow': {'file_key_val': False, 'meta': '-'},
    'verbose': {'file_key_val': True, 'meta': '+'}}

assert build_diff_lst(diff_dic) == [
    "- {'follow': False}",
    "  {'host': 'hexlet.io'}",
    "- {'proxy': '123.234.53.22'}",
    "- {'timeout': 50}\n+ {'timeout': 20}",
    "+ {'verbose': True}"]

assert generate_diff(path1, path2) == '''{
- {'follow': False}
  {'host': 'hexlet.io'}
- {'proxy': '123.234.53.22'}
- {'timeout': 50}
+ {'timeout': 20}
+ {'verbose': True}
}'''