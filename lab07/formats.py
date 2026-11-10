import json


def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return []
    lines = text.splitlines()
    header = [h.strip() for h in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        records.append({header[i]: values[i] for i in range(len(header))})
    return records


def _scalar(value: str):
    low = value.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current = None
    for raw in lines:
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        s = line.strip()
        if s.startswith("- "):
            if current is not None:
                result[current].append(_scalar(s[2:].strip()))
        elif ":" in s:
            key, _, value = s.partition(":")
            key = key.strip()
            value = value.strip()
            if value == "":
                current = key
                result[key] = []
            else:
                current = None
                result[key] = _scalar(value)
    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []
    for row in rows:
        addition = extra.get(row.get(key))
        if isinstance(addition, dict):
            result.append({**addition, **row})
        else:
            result.append(dict(row))
    return result


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)