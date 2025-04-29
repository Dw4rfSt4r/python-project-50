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


def test_format_stylish_nested():
    nested_diff = {
        "common": {
            "status": "nested",
            "children": {
                "follow": {
                    "status": "added",
                    "value": False
                },
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
                },
                "setting4": {
                    "status": "added",
                    "value": "blah blah"
                },
                "setting5": {
                    "status": "added",
                    "value": {
                        "key5": "value5"
                    }
                },
                "setting6": {
                    "status": "nested",
                    "children": {
                        "key": {
                            "status": "unchanged",
                            "value": "value"
                        },
                        "ops": {
                            "status": "added",
                            "value": "vops"
                        },
                        "doge": {
                            "status": "nested",
                            "children": {
                                "wow": {
                                    "status": "changed",
                                    "old_value": "",
                                    "new_value": "so much"
                                }
                            }
                        }
                    }
                }
            }
        },
        "group1": {
            "status": "nested",
            "children": {
                "baz": {
                    "status": "changed",
                    "old_value": "bas",
                    "new_value": "bars"
                },
                "foo": {
                    "status": "unchanged",
                    "value": "bar"
                },
                "nest": {
                    "status": "changed",
                    "old_value": {
                        "key": "value"
                    },
                    "new_value": "str"
                }
            }
        },
        "group2": {
            "status": "removed",
            "value": {
                "abc": 12345,
                "deep": {
                    "id": 45
                }
            }
        },
        "group3": {
            "status": "added",
            "value": {
                "deep": {
                    "id": {
                        "number": 45
                    }
                },
                "fee": 100500
            }
        }
    }

    expected_output = (
        "{\n"
        "    common: {\n"
        "      + follow: false\n"
        "        setting1: Value 1\n"
        "      - setting2: 200\n"
        "      - setting3: true\n"
        "      + setting3: null\n"
        "      + setting4: blah blah\n"
        "      + setting5: {\n"
        "            key5: value5\n"
        "        }\n"
        "        setting6: {\n"
        "            doge: {\n"
        "              - wow: \n"
        "              + wow: so much\n"
        "            }\n"
        "            key: value\n"
        "          + ops: vops\n"
        "        }\n"
        "    }\n"
        "    group1: {\n"
        "      - baz: bas\n"
        "      + baz: bars\n"
        "        foo: bar\n"
        "      - nest: {\n"
        "            key: value\n"
        "        }\n"
        "      + nest: str\n"
        "    }\n"
        "  - group2: {\n"
        "        abc: 12345\n"
        "        deep: {\n"
        "            id: 45\n"
        "        }\n"
        "    }\n"
        "  + group3: {\n"
        "        deep: {\n"
        "            id: {\n"
        "                number: 45\n"
        "            }\n"
        "        }\n"
        "        fee: 100500\n"
        "    }\n"
        "}"
    )

    assert format_stylish(nested_diff) == expected_output
