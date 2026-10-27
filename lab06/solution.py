def count_by_extension(paths):
    result = {}
    for path in paths:
        name = path.split("/")[-1]
        if "." in name:
            ext = name.split(".")[-1].lower()
        else:
            ext = ""
        if ext in result:
            result[ext] = result[ext] + 1
        else:
            result[ext] = 1
    return result


def deepest_path(paths):
    if len(paths) == 0:
        return ""
    best = paths[0]
    for path in paths:
        if path.count("/") > best.count("/"):
            best = path
        elif path.count("/") == best.count("/"):
            if path < best:
                best = path
    return best


def human_size(n_bytes):
    if n_bytes < 1024:
        return str(n_bytes) + " Б"
    size = n_bytes / 1024
    if size < 1024:
        return f"{size:.1f} КБ"
    size = size / 1024
    if size < 1024:
        return f"{size:.1f} МБ"
    size = size / 1024
    if size < 1024:
        return f"{size:.1f} ГБ"
    size = size / 1024
    return f"{size:.1f} ТБ"

