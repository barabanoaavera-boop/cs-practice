def parse_event(line: str) -> dict:
    parts = line.split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError("Ожидается время, уровень и сообщение")
    time, level, message = parts
    if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
        raise ValueError(f"Неизвестный уровень: {level!r}")
    if not time or not message:
        raise ValueError("Пустое время или сообщение")
    return {"time": time, "level": level, "message": message.strip()}


def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n: int) -> list:
    messages = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            msg = event["message"]
            messages[msg] = messages.get(msg, 0) + 1
    pairs = [[msg, cnt] for msg, cnt in messages.items()]
    pairs.sort(key=lambda p: (-p[1], p[0]))
    return pairs[:n]


def format_report(counts: dict, errors: list) -> str:
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    for msg, cnt in errors:
        lines.append(f"- {msg} — {cnt}")
    lines.append("")
    return "\n".join(lines)
