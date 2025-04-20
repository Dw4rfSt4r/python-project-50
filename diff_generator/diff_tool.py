def process_flat_files(file1: dict, file2: dict) -> dict:
    # Create an empty dictionary to store differences
    inner_diff = {}
    # Get all keys from both dictionaries
    all_keys = set(file1.keys()) | set(file2.keys())
    for key in all_keys:
        if key in file1 and key in file2:
            # If key exists in both dictionaries
            if file1[key] == file2[key]:
                # If values are the same
                inner_diff[key] = {
                    'status': 'unchanged',
                    'value': file1[key]}
            else:
                # If values are different
                inner_diff[key] = {
                    'status': 'changed',
                    'old_value': file1[key],
                    'new_value': file2[key]}
        elif key in file2:
            # If key only exists in the second dictionary
            inner_diff[key] = {'status': 'added',
                               'value': file2[key]}
        else:
            # If key only exists in the first dictionary
            inner_diff[key] = {'status': 'removed',
                               'value': file1[key]}
    return inner_diff
