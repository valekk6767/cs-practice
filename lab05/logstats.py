LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


def parse_event(line):
    line = line.strip()
    parts = line.split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("не хватает частей в строке")

    time, level, message = parts

    if level not in LEVELS:
        raise ValueError("неизвестный уровень: " + level)

    return {"time": time, "level": level, "message": message}


def count_levels(lines):
    counts = {}

    for line in lines:
        if line.strip() == "":
            continue

        try:
            event = parse_event(line)
            level = event["level"]
        except ValueError:
            level = "BROKEN"

        counts[level] = counts.get(level, 0) + 1

    return counts


def top_errors(lines, n):
    counter = {}

    for line in lines:
        if line.strip() == "":
            continue

        try:
            event = parse_event(line)
        except ValueError:
            continue

        if event["level"] != "ERROR":
            continue

        msg = event["message"]
        counter[msg] = counter.get(msg, 0) + 1

    items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    result = []
    for msg, cnt in items[:n]:
        result.append([msg, cnt])

    return result


def format_report(counts, errors):
    lines = []
    lines.append("Отчёт по журналу")
    lines.append("")

    for level in sorted(counts):
        lines.append("{}: {}".format(level, counts[level]))

    lines.append("")
    lines.append("Частые ошибки:")

    for msg, cnt in errors:
        lines.append("- {} — {}".format(msg, cnt))

    return "\n".join(lines) + "\n"