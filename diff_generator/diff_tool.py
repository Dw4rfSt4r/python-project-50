def process_nested_files(file1: dict, file2: dict) -> dict:

    def build_diff(dict1, dict2):
        # Get all keys from both dictionaries
        all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
        result = {}
        
        for key in all_keys:
            # If key exists in both dictionaries
            if key in dict1 and key in dict2:
                # If both values are dictionaries, recursively process them
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                    result[key] = {
                        'status': 'nested',
                        'children': build_diff(dict1[key], dict2[key])
                    }
                # If values are the same
                elif dict1[key] == dict2[key]:
                    result[key] = {
                        'status': 'unchanged',
                        'value': dict1[key]
                    }
                # If values are different
                else:
                    result[key] = {
                        'status': 'changed',
                        'old_value': dict1[key],
                        'new_value': dict2[key]
                    }
            # If key only exists in the second dictionary
            elif key in dict2:
                result[key] = {
                    'status': 'added',
                    'value': dict2[key]
                }
            # If key only exists in the first dictionary
            else:
                result[key] = {
                    'status': 'removed',
                    'value': dict1[key]
                }
        
        return result
    
    # Start the recursive comparison
    return build_diff(file1, file2)


process_flat_files = process_nested_files
