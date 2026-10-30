import json


def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().splitlines()
    if not lines:
        return []
    headers = lines[0].split(",")
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = line.split(",")
        record = {}
        for i in range(len(headers)):
            record[headers[i]] = values[i] if i < len(values) else ""
        records.append(record)
    return records


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list_key = None
    
    for line in lines:
        if not line.strip():
            continue
        if "#" in line:
            line = line.split("#")[0]
        line = line.rstrip()
        if not line.strip():
            continue
            
        if line.startswith("  - ") or line.startswith("- "):
            val = line.split("- ", 1)[1].strip()
            val = _convert_type(val)
            if current_list_key is not None:
                result[current_list_key].append(val)
            continue
            
        if ":" in line:
            parts = line.split(":", 1)
            key = parts[0].strip()
            value = parts[1].strip()
            
            if value == "":
                current_list_key = key
                result[key] = []
            else:
                current_list_key = None
                result[key] = _convert_type(value)
    return result


def _convert_type(val: str):
    if val.lower() in ("true", "yes"):
        return True
    if val.lower() in ("false", "no"):
        return False
    try:
        if "." in val:
            return float(val)
        return int(val)
    except ValueError:
        return val


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []
    for row in rows:
        row_copy = row.copy()
        lookup = str(row.get(key, ""))
        if lookup in extra:
            for k, v in extra[lookup].items():
                if k not in row_copy:
                    row_copy[k] = v
        result.append(row_copy)
    return result


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
