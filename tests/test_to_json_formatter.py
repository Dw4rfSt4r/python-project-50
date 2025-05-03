import json

from gendiff.formatters.to_json_formatter import json_formatter


def test_json_formatter_simple_diff():
    diff = {
        "host": {
            "status": "unchanged",
            "value": "hexlet.io"
        },
        "timeout": {
            "status": "changed",
            "old_value": 50,
            "new_value": 20
        },
        "proxy": {
            "status": "removed",
            "value": "123.234.53.22"
        },
        "verbose": {
            "status": "added",
            "value": True
        }
    }
    expected_output = json.dumps(diff, indent=4, sort_keys=True)
    assert json_formatter(diff) == expected_output


def test_json_formatter_nested_diff():
    diff = {
        "common": {
            "status": "nested",
            "children": {
                "setting1": {
                    "status": "unchanged",
                    "value": "Value 1"
                },
                "setting2": {
                    "status": "removed",
                    "value": 200
                },
                "setting3": {
                    "status": "changed",
                    "old_value": True,
                    "new_value": None
                }
            }
        }
    }
    expected_output = json.dumps(diff, indent=4, sort_keys=True)
    assert json_formatter(diff) == expected_output


def test_json_formatter_empty_diff():
    diff = {}
    expected_output = json.dumps(diff, indent=4, sort_keys=True)
    assert json_formatter(diff) == expected_output
