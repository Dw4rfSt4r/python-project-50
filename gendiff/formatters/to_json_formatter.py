import json


def json_formatter(diff):
    return json.dumps(diff, indent=4, sort_keys=True)