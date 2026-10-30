import json


def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().splitlines()
    if not lines:
        return []
    headers = [h.strip() for h in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
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
        # 1. Отбрасываем комментарии (всё после #)
        if "#" in line:
            line = line.split("#")[0]
        # 2. Убираем пробелы по краям
        line = line.strip()
        if not line:
            continue
            
        # 3. Проверяем на элемент списка
        if line.startswith("- "):
            val = line[2:].strip()
            val = _convert_type(val)
            if current_list_key is not None:
                result[current_list_key].append(val)
            continue
            
        # 4. Проверяем на пару ключ: значение
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
    lower_val = val.lower()
    if lower_val in ("true", "yes"):
        return True
    if lower_val in ("false", "no"):
        return False
    
    # Пограничный случай: если внутри есть запятая (3,5) — это не число по правилам YAML, а строка
    if "," in val:
        return val
        
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
