
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
    return ("{\n" + "\n".join(result) + "\n}").lower()

