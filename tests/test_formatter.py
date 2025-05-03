from diff_generator.formatter import format_plain, format_stylish

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


def test_format_plain():
    expected_output = (
    "Property 'common.follow' was added with value: false\n"
    "Property 'common.setting2' was removed\n"
    "Property 'common.setting3' was updated. From true to null\n"
    "Property 'common.setting4' was added with value: 'blah blah'\n"
    "Property 'common.setting5' was added with value: [complex value]\n"
    "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n"
    "Property 'common.setting6.ops' was added with value: 'vops'\n"
    "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
    "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
    "Property 'group2' was removed\n"
    "Property 'group3' was added with value: [complex value]"
    )
    assert format_plain(nested_diff) == expected_output


def test_format_stylish_empty():
    diff = {}
    expected_output = "{\n}"
    assert format_stylish(diff) == expected_output


def test_format_stylish_unchanged_single_key():
    diff = {
        "key": {"status": "unchanged", "value": "value"}
    }
    expected_output = (
        "{\n"
        "    key: value\n"
        "}"
    )
    assert format_stylish(diff) == expected_output


def test_format_stylish_nested_empty_children():
    diff = {
        "parent": {"status": "nested", "children": {}}
    }
    expected_output = (
        "{\n"
        "    parent: {\n"
        "    }\n"
        "}"
    )
    assert format_stylish(diff) == expected_output


def test_format_plain_empty():
    diff = {}
    expected_output = ""
    assert format_plain(diff) == expected_output


def test_format_plain_unchanged_single_key():
    diff = {
        "key": {"status": "unchanged", "value": "value"}
    }
    expected_output = ""
    assert format_plain(diff) == expected_output


def test_format_plain_added_none_value():
    diff = {
        "key": {"status": "added", "value": None}
    }
    expected_output = "Property 'key' was added with value: null"
    assert format_plain(diff) == expected_output
