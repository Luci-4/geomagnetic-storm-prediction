def get_all_keys(d):
    keys = []
    for k, v in d.items():
        if isinstance(v, dict):
            keys.extend(get_all_keys(v))
        else:
            keys.append(k)
    return keys
