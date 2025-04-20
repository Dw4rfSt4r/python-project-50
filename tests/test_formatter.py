from diff_generator.formatter import format_stylish


def test_format_stylish():
    diff = {
        "host": {"status": "unchanged", "value": "hexlet.io"},
        "timeout": {"status": "changed", "old_value": 50, "new_value": 20},
        "proxy": {"status": "removed", "value": "123.234.53.22"},
        "follow": {"status": "removed", "value": False},
        "verbose": {"status": "added", "value": True}
    }

    expected_output = (
        "{\n"
        "  - follow: false\n"
        "    host: hexlet.io\n"
        "  - proxy: 123.234.53.22\n"
        "  - timeout: 50\n"
        "  + timeout: 20\n"
        "  + verbose: true\n"
        "}"
    )

    assert format_stylish(diff) == expected_output
