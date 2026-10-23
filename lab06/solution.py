def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        name = path.split("/")[-1]
        if name.startswith(".") and name.count(".") == 1:
            ext = ""
        elif "." in name:
            ext = name.split(".")[-1].lower()
        else:
            ext = ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))


def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    units = ["КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    for unit in units:
        size /= 1024.0
        if size < 1024.0:
            return f"{size:.1f} {unit}"
    return f"{size:.1f} ТБ"
