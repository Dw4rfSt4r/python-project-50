def format_plain(diff: dict, parent_key: str = "") -> str:
    """
    Format the difference dictionary in plain text format.
    
    Args:
        diff: Dictionary with differences
        parent_key: Accumulated key path for nested structures
        
    Returns:
        Formatted string representation of differences
    """
    lines = []
    
    for key in sorted(diff.keys()):
        current_key = f"{parent_key}.{key}" if parent_key else key
        value = diff[key]
        status = value["status"]
        
        if status == "nested":
            lines.append(format_plain(value["children"], current_key))
        elif status == "unchanged":
            continue
        elif status == "removed":
            lines.append(
            f"Property '{current_key}' was removed"
            )
        elif status == "added":
            val = _format_plain_value(value["value"])
            lines.append(
            f"Property '{current_key}' was added with value: {val}"
            )
        elif status == "changed":
            old_val = _format_plain_value(value["old_value"])
            new_val = _format_plain_value(value["new_value"])
            lines.append(
            f"Property '{current_key}' was updated. From {old_val} to {new_val}"
            )
    
    return "\n".join(lines)


def _format_plain_value(value) -> str:
    """Format a value for plain output."""
    if isinstance(value, (dict, list)):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)