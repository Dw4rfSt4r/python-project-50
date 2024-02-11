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
inner_dif_json = generate_inner_dif(file1, file2)
inner_dif_yml = generate_inner_dif(file3, file4)


def test_generate_inner_dif():
    assert generate_inner_dif(file1, file2) == {
        'follow': {'value': False, 'meta': '-'},
        'proxy': {'value': '123.234.53.22', 'meta': '-'},
        'verbose': {'value': True, 'meta': '+'},
        'timeout': {'value': (50, 20), 'meta': 'modified'},
        'host': {'value': 'hexlet.io', 'meta': 'match'}}

    assert generate_inner_dif(file3, file4) == {
        'follow': {'value': False, 'meta': '-'},
        'proxy': {'value': '123.234.53.22', 'meta': '-'},
        'verbose': {'value': True, 'meta': '+'},
        'timeout': {'value': (50, 20), 'meta': 'modified'},
        'host': {'value': 'hexlet.io', 'meta': 'match'}}

    assert generate_inner_dif(nstd_jsn1, nstd_jsn2) == {
        'group2': {
            'value': {'abc': 12345, 'deep': {'id': 45}}, 'meta': '-'},
        'group3': {
            'value': {'deep': {'id': {'number': 45}},
                      'fee': 100500}, 'meta': '+'},
        'group1': {
            'value': {
                'foo': {'value': 'bar', 'meta': 'match'},
                'baz': {'value': ('bas', 'bars'), 'meta': 'modified'},
                'nest': {'value': ({'key': 'value'}, 'str'),
                         'meta': 'modified'}},
            'meta': 'modified'},
        'common': {'value': {
            'setting2': {'value': 200, 'meta': '-'},
            'follow': {'value': False, 'meta': '+'},
            'setting5': {'value': {'key5': 'value5'}, 'meta': '+'},
            'setting4': {'value': 'blah blah', 'meta': '+'},
            'setting1': {'value': 'Value 1', 'meta': 'match'},
            'setting6': {'value': {
                'ops': {'value': 'vops', 'meta': '+'},
                'doge': {'value': {
                    'wow': {'value': ('', 'so much'),
                            'meta': 'modified'}},
                         'meta': 'modified'},
                'key': {'value': 'value', 'meta': 'match'}},
                'meta': 'modified'},
            'setting3': {'value': (True, None),
                         'meta': 'modified'}}, 'meta': 'modified'}}

    assert generate_inner_dif(nstd_yml1, nstd_yml2) == {
        'group2': {
            'value': {'abc': 12345, 'deep': {'id': 45}}, 'meta': '-'},
        'group3': {
            'value': {'deep': {'id': {'number': 45}},
                      'fee': 100500}, 'meta': '+'},
        'group1': {
            'value': {
                'foo': {'value': 'bar', 'meta': 'match'},
                'baz': {'value': ('bas', 'bars'), 'meta': 'modified'},
                'nest': {'value': ({'key': 'value'}, 'str'),
                         'meta': 'modified'}},
            'meta': 'modified'},
        'common': {'value': {
            'setting2': {'value': 200, 'meta': '-'},
            'follow': {'value': False, 'meta': '+'},
            'setting5': {'value': {'key5': 'value5'}, 'meta': '+'},
            'setting4': {'value': 'blah blah', 'meta': '+'},
            'setting1': {'value': 'Value 1', 'meta': 'match'},
            'setting6': {'value': {
                'ops': {'value': 'vops', 'meta': '+'},
                'doge': {'value': {
                    'wow': {'value': ('', 'so much'),
                            'meta': 'modified'}},
                         'meta': 'modified'},
                'key': {'value': 'value', 'meta': 'match'}},
                'meta': 'modified'},
            'setting3': {'value': (True, None),
                         'meta': 'modified'}}, 'meta': 'modified'}}


def test_format_diff_to_lst():
    assert format_diff_to_lst(inner_dif_json) == [
        "- {'follow': false}",
        "  {'host': 'hexlet.io'}",
        "- {'proxy': '123.234.53.22'}",
        "- {'timeout': 50}\n+ {'timeout': 20}",
        "+ {'verbose': True}"]

    assert format_diff_to_lst(inner_dif_yml) == [
        "- {'follow': false}",
        "  {'host': 'hexlet.io'}",
        "- {'proxy': '123.234.53.22'}",
        "- {'timeout': 50}\n+ {'timeout': 20}",
        "+ {'verbose': True}"]


def test_generate_diff():
    assert generate_diff(path1, path2) == """{\n- {'follow': false}\n  {'host': 'hexlet.io'}\n- {'proxy': '123.234.53.22'}\n- {'timeout': 50}\n+ {'timeout': 20}\n+ {'verbose': True}\n}"""

    assert generate_diff(path3, path4) == """{\n- {'follow': false}\n  {'host': 'hexlet.io'}\n- {'proxy': '123.234.53.22'}\n- {'timeout': 50}\n+ {'timeout': 20}\n+ {'verbose': True}\n}"""
