def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError("неверный формат строки")
    time_str, level, message = parts
    if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
        raise ValueError("неизвестный уровень лога")
    return {"time": time_str, "level": level, "message": message}

def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            parsed = parse_event(line)
            lvl = parsed["level"]
            counts[lvl] = counts.get(lvl, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
    return counts