def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for p in paths:
        filename = p.split('/')[-1]
        last_dot = filename.rfind('.')
        if last_dot <= 0:
            ext = ""
        else:
            ext = filename[last_dot + 1:].lower()
        counts[ext] = counts.get(ext, 0) + 1
    return counts

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    sorted_paths = sorted(paths)
    return max(sorted_paths, key=lambda p: p.count('/'))


def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    size = n_bytes / 1024
    for unit in ["КБ", "МБ", "ГБ", "ТБ"]:
        if size < 1024 or unit == "ТБ":
            return f"{size:.1f} {unit}"
        size /= 1024