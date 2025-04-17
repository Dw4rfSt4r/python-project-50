"""
    def choose_formatter(format: str):
    if format == "stylish":
        return stylish
    elif format == "plain":
        return plain
    elif format == "json":
        return json
    else:
        raise ValueError(f"Unknown format: {format}")
"""
def format_stylish(diff: dict) -> str:
    result = []
    sorted_keys = sorted(diff.keys())
    for key in sorted_keys:
        value = diff[key]
        if value["status"] == "unchanged":
            result.append(f"    {key}: {value['value']}")
        elif value["status"] == "changed":
            result.append(f"  - {key}: {value['old_value']}")
            result.append(f"  + {key}: {value['new_value']}")
        elif value["status"] == "removed":
            result.append(f"  - {key}: {value['value']}")
        elif value["status"] == "added":
            result.append(f"  + {key}: {value['value']}")
    print(result)
    return ("{\n" + "\n".join(result) + "\n}").lower()


diff = {
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

print(format_stylish(diff))