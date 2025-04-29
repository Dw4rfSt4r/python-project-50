from diff_generator.arg_parser import read_file
from diff_generator.diff_tool import process_nested_files

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
    assert process_nested_files(json1, json2) == expected
    assert process_nested_files(yml1, yml2) == expected
    assert process_nested_files(json1, yml2) == expected
    

def test_process_nested_files():
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

    assert process_nested_files(nested_json_1, nested_json_2) == expected
    assert process_nested_files(nested_yml_1, nested_yml_2) == expected