from gendiff.arg_parser import read_file, validate_file_ext
from gendiff.formatters.stylish_formatter import format_stylish
from gendiff.formatters.plain_formatter import format_plain
from gendiff.formatters.to_json_formatter import json_formatter


def build_diff(file1: dict, file2: dict) -> dict:

    def build_diff_recursive(dict1, dict2):
        all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
        result = {}

        for key in all_keys:
            if key in dict1 and key in dict2:
                is_dict1 = isinstance(dict1[key], dict)
                is_dict2 = isinstance(dict2[key], dict)
                if is_dict1 and is_dict2:
                    result[key] = {
                        'status': 'nested',
                        'children': build_diff_recursive(dict1[key], dict2[key])
                    }
                elif dict1[key] == dict2[key]:
                    result[key] = {
                        'status': 'unchanged',
                        'value': dict1[key]
                    }
                else:
                    result[key] = {
                        'status': 'changed',
                        'old_value': dict1[key],
                        'new_value': dict2[key]
                    }
            elif key in dict2:
                result[key] = {
                    'status': 'added',
                    'value': dict2[key]
                }
            else:
                result[key] = {
                    'status': 'removed',
                    'value': dict1[key]
                }

        return result

    return build_diff_recursive(file1, file2)


def generate_diff(file1, file2, format_name='stylish'):
    if isinstance(file1, str) and isinstance(file2, str):
        validate_file_ext(file1, file2)
        file1 = read_file(file1)
        file2 = read_file(file2)

    diff = build_diff(file1, file2)

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return json_formatter(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")
