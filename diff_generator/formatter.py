def format_value(value, depth=0):
    """Format a value for stylish output with proper indentation."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if value == "":
        return ""
    if not isinstance(value, dict):
        return str(value)
    
    indent = "    " * depth
    lines = ["{"]
    
    for key in sorted(value.keys()):
        formatted_value = format_value(value[key], depth + 1)
        lines.append(f"{indent}    {key}: {formatted_value}")
    
    lines.append(f"{indent}}}")
    return "\n".join(lines)


def format_stylish(diff: dict, depth=0) -> str:
    """
    Format the difference dictionary in a stylish way.
    
    Args:
        diff: Dictionary with differences
        depth: Current depth level for indentation
        
    Returns:
        Formatted string representation of differences
    """
    indent = "    " * depth
    result = ["{"]
    
    for key in sorted(diff.keys()):
        value = diff[key]
        status = value["status"]
        
        if status == "nested":
            children = format_stylish(value["children"], depth + 1)
            result.append(f"{indent}    {key}: {children}")
        elif status == "unchanged":
            formatted_value = format_value(value["value"], depth + 1)
            result.append(f"{indent}    {key}: {formatted_value}")
        elif status == "changed":
            old_formatted = format_value(value["old_value"], depth + 1)
            new_formatted = format_value(value["new_value"], depth + 1)
            result.append(f"{indent}  - {key}: {old_formatted}")
            result.append(f"{indent}  + {key}: {new_formatted}")
        elif status == "removed":
            formatted_value = format_value(value["value"], depth + 1)
            result.append(f"{indent}  - {key}: {formatted_value}")
        elif status == "added":
            formatted_value = format_value(value["value"], depth + 1)
            result.append(f"{indent}  + {key}: {formatted_value}")
    
    result.append(f"{indent}}}")
    return "\n".join(result)


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