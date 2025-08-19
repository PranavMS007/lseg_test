def get_value(nested_dict, key_path):
    """
    Traverse a nested dictionary using a '/' delimited key path.
    
    Arguments:
        nested_dict (dict): The dictionary to search.
        key_path (str): Slash-delimited string of keys to traverse.
        
    Returns:
        The value found at the provided path, or None if the path is invalid.
    """
    keys = key_path.split("/")
    current = nested_dict
    
    for k in keys:
        if isinstance(current, dict) and k in current:
            current = current[k]
        else:
            return None  # key not found / invalid path
    return current


def test_get_value():
    obj1 = {"a": {"b": {"c": "d"}}}
    obj2 = {"x": {"y": {"z": "a"}}}
    obj3 = {"foo": {"bar": 123}, "baz": "hello"}
    
    assert get_value(obj1, "a/b/c") == "d"
    assert get_value(obj2, "x/y/z") == "a"
    assert get_value(obj3, "foo/bar") == 123
    assert get_value(obj3, "baz") == "hello"
    
    # failure cases
    assert get_value(obj1, "a/x/c") is None
    assert get_value(obj3, "foo/bar/baz") is None
    
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_get_value()