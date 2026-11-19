import json


def csv_to_records(text: str) -> list[dict]:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    headers = [h.strip() for h in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        values = [v.strip() for v in line.split(",")]
        records.append(dict(zip(headers, values)))
    return records


def _parse_value(raw: str):
    low = raw.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    try:
        return int(raw)
    except ValueError:
        pass
    try:
        return float(raw)
    except ValueError:
        return raw


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list = None
    for line in lines:
        clean = line.split("#", 1)[0].strip()
        if not clean:
            continue
        if clean.startswith("- ") and current_list is not None:
            current_list.append(_parse_value(clean[2:].strip()))
        elif ":" in clean:
            key, value = clean.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value == "":
                result[key] = []
                current_list = result[key]
            else:
                result[key] = _parse_value(value)
                current_list = None
    return result