from gendiff.gendiff_pac import generate_diff, generate_inner_dif
from gendiff.gendiff_pac import get_files, format_diff_to_lst


path1 = 'tests/fixtures/file1.json'
path2 = 'tests/fixtures/file2.json'
path3 = 'tests/fixtures/file3.yml'
path4 = 'tests/fixtures/file4.yaml'
pth_nstd_jsn1 = 'tests/fixtures/file_nested_1.json'
pth_nstd_jsn2 = 'tests/fixtures/file_nested_2.json'
pth_nstd_yml1 = 'tests/fixtures/file_nested_1.yml'
pth_nstd_yml2 = 'tests/fixtures/file_nested_2.yaml'

file1, file2 = get_files(path1, path2)
file3, file4 = get_files(path3, path4)
nstd_jsn1, nstd_jsn2 = get_files(pth_nstd_jsn1, pth_nstd_jsn2)
nstd_yml1, nstd_yml2 = get_files(pth_nstd_yml1, pth_nstd_yml2)
diff_dic_json = generate_inner_dif(file1, file2)
diff_dic_yml = generate_inner_dif(file3, file4)


def test_generate_inner_dif():
    assert generate_inner_dif(file1, file2) == {
        'follow': {'file_key_val': False, 'meta': '-'},
        'proxy': {'file_key_val': '123.234.53.22', 'meta': '-'},
        'verbose': {'file_key_val': True, 'meta': '+'},
        'timeout': {'file_key_val': (50, 20), 'meta': 'modified'},
        'host': {'file_key_val': 'hexlet.io', 'meta': 'match'}}

    assert generate_inner_dif(file3, file4) == {
        'follow': {'file_key_val': False, 'meta': '-'},
        'proxy': {'file_key_val': '123.234.53.22', 'meta': '-'},
        'verbose': {'file_key_val': True, 'meta': '+'},
        'timeout': {'file_key_val': (50, 20), 'meta': 'modified'},
        'host': {'file_key_val': 'hexlet.io', 'meta': 'match'}}

    assert generate_inner_dif(nstd_jsn1, nstd_jsn2) == {
        'group2': {
            'file_key_val': {'abc': 12345, 'deep': {'id': 45}}, 'meta': '-'},
        'group3': {
            'file_key_val': {'deep': {'id': {'number': 45}},
                             'fee': 100500}, 'meta': '+'},
        'group1': {
            'file_key_val': {
                'foo': {'file_key_val': 'bar', 'meta': 'match'},
                'baz': {'file_key_val': ('bas', 'bars'), 'meta': 'modified'},
                'nest': {'file_key_val': ({'key': 'value'}, 'str'),
                         'meta': 'modified'}},
            'meta': 'modified'},
        'common': {'file_key_val': {
            'setting2': {'file_key_val': 200, 'meta': '-'},
            'follow': {'file_key_val': False, 'meta': '+'},
            'setting5': {'file_key_val': {'key5': 'value5'}, 'meta': '+'},
            'setting4': {'file_key_val': 'blah blah', 'meta': '+'},
            'setting1': {'file_key_val': 'Value 1', 'meta': 'match'},
            'setting6': {'file_key_val': {
                'ops': {'file_key_val': 'vops', 'meta': '+'},
                'doge': {'file_key_val': {
                    'wow': {'file_key_val': ('', 'so much'),
                            'meta': 'modified'}},
                         'meta': 'modified'},
                'key': {'file_key_val': 'value', 'meta': 'match'}},
                'meta': 'modified'},
            'setting3': {'file_key_val': (True, None),
                         'meta': 'modified'}}, 'meta': 'modified'}}
    
    assert generate_inner_dif(nstd_yml1, nstd_yml2) == {
        'group2': {
            'file_key_val': {'abc': 12345, 'deep': {'id': 45}}, 'meta': '-'},
        'group3': {
            'file_key_val': {'deep': {'id': {'number': 45}},
                             'fee': 100500}, 'meta': '+'},
        'group1': {
            'file_key_val': {
                'foo': {'file_key_val': 'bar', 'meta': 'match'},
                'baz': {'file_key_val': ('bas', 'bars'), 'meta': 'modified'},
                'nest': {'file_key_val': ({'key': 'value'}, 'str'),
                         'meta': 'modified'}},
            'meta': 'modified'},
        'common': {'file_key_val': {
            'setting2': {'file_key_val': 200, 'meta': '-'},
            'follow': {'file_key_val': False, 'meta': '+'},
            'setting5': {'file_key_val': {'key5': 'value5'}, 'meta': '+'},
            'setting4': {'file_key_val': 'blah blah', 'meta': '+'},
            'setting1': {'file_key_val': 'Value 1', 'meta': 'match'},
            'setting6': {'file_key_val': {
                'ops': {'file_key_val': 'vops', 'meta': '+'},
                'doge': {'file_key_val': {
                    'wow': {'file_key_val': ('', 'so much'),
                            'meta': 'modified'}},
                         'meta': 'modified'},
                'key': {'file_key_val': 'value', 'meta': 'match'}},
                'meta': 'modified'},
            'setting3': {'file_key_val': (True, None),
                         'meta': 'modified'}}, 'meta': 'modified'}}


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
    assert generate_diff(path1, path2) == """{\n- {'follow': false}\n  {'host': 'hexlet.io'}\n- {'proxy': '123.234.53.22'}\n- {'timeout': 50}\n+ {'timeout': 20}\n+ {'verbose': True}\n}"""

    assert generate_diff(path3, path4) == """{\n- {'follow': false}\n  {'host': 'hexlet.io'}\n- {'proxy': '123.234.53.22'}\n- {'timeout': 50}\n+ {'timeout': 20}\n+ {'verbose': True}\n}"""
