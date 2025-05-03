import pytest

from gendiff.arg_parser import read_file
from gendiff.diff_tool import build_diff, generate_diff

json1 = read_file("tests/test_data/flat_1.json")
json2 = read_file("tests/test_data/flat_2.json")
yml1 = read_file("tests/test_data/flat_1.yml")
yml2 = read_file("tests/test_data/flat_2.yaml")
nested_json_1 = read_file("tests/test_data/nested_1.json")
nested_json_2 = read_file("tests/test_data/nested_2.json")
nested_yml_1 = read_file("tests/test_data/nested_1.yaml")
nested_yml_2 = read_file("tests/test_data/nested_2.yml")


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
    assert build_diff(json1, json2) == expected
    assert build_diff(yml1, yml2) == expected
    assert build_diff(json1, yml2) == expected


def test_build_diff():
    expected = {
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
    assert build_diff(nested_json_1, nested_json_2) == expected
    assert build_diff(nested_yml_1, nested_yml_2) == expected


def test_build_diff_empty():
    assert build_diff({}, {}) == {}


def test_build_diff_unchanged_single_key():
    dict1 = {"key": "value"}
    dict2 = {"key": "value"}
    expected = {
        "key": {
            "status": "unchanged",
            "value": "value"
        }
    }
    assert build_diff(dict1, dict2) == expected


def test_build_diff_added_key():
    dict1 = {}
    dict2 = {"key": "value"}
    expected = {
        "key": {
            "status": "added",
            "value": "value"
        }
    }
    assert build_diff(dict1, dict2) == expected


def test_build_diff_removed_key():
    dict1 = {"key": "value"}
    dict2 = {}
    expected = {
        "key": {
            "status": "removed",
            "value": "value"
        }
    }
    assert build_diff(dict1, dict2) == expected


def test_build_diff_changed_key():
    dict1 = {"key": "value1"}
    dict2 = {"key": "value2"}
    expected = {
        "key": {
            "status": "changed",
            "old_value": "value1",
            "new_value": "value2"
        }
    }
    assert build_diff(dict1, dict2) == expected


def test_build_diff_nested_empty_children():
    dict1 = {"parent": {}}
    dict2 = {"parent": {}}
    expected = {
        "parent": {
            "status": "nested",
            "children": {}
        }
    }
    assert build_diff(dict1, dict2) == expected


def test_build_diff_invalid_inputs():
    with pytest.raises(AttributeError):
        build_diff("not a dict", {"key": "value"})

    with pytest.raises(AttributeError):
        build_diff({"key": "value"}, 123)

    with pytest.raises(AttributeError):
        build_diff(None, None)


def test_generate_diff_non_existent_files():
    try:
        generate_diff("nonexistent_file1.json", "nonexistent_file2.json")
        assert False, "Expected Exception"
    except Exception:
        pass


def test_build_diff_with_none_values():
    """Test build_diff with None values."""
    dict1 = {"key1": None, "key2": "value"}
    dict2 = {"key1": "value", "key2": None}
    expected = {
        "key1": {
            "status": "changed",
            "old_value": None,
            "new_value": "value"
        },
        "key2": {
            "status": "changed",
            "old_value": "value",
            "new_value": None
        }
    }
    assert build_diff(dict1, dict2) == expected


def test_build_diff_with_boolean_values():
    """Test build_diff with boolean values."""
    dict1 = {"key1": True, "key2": False}
    dict2 = {"key1": False, "key2": True}
    expected = {
        "key1": {
            "status": "changed",
            "old_value": True,
            "new_value": False
        },
        "key2": {
            "status": "changed",
            "old_value": False,
            "new_value": True
        }
    }
    assert build_diff(dict1, dict2) == expected


def test_generate_diff_with_same_files():
    """Test generate_diff with identical files."""
    output = generate_diff(
        "tests/test_data/flat_1.json", 
        "tests/test_data/flat_1.json"
    )
    assert "+" not in output
    assert "-" not in output
