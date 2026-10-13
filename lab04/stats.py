"""Модуль обработки записей метеостанции."""


def parse_record(line: str) -> dict:
    """Разбирает строку «город;температура;дата» в словарь.

    Возвращает {"city": str, "temp": float, "date": str}.
    Негодная строка — ValueError с понятным сообщением.
    """
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(
            f"ожидалось 3 поля через ';', получено {len(parts)}: {line!r}"
        )

    city, temp_raw, date = parts

    if not city.strip():
        raise ValueError(f"пустой город: {line!r}")
    if not date.strip():
        raise ValueError(f"пустая дата: {line!r}")

    try:
        temp = float(temp_raw)
    except ValueError as exc:
        raise ValueError(f"температура не число: {temp_raw!r}") from exc

    return {"city": city.strip(), "temp": temp, "date": date.strip()}


def read_valid(lines: list[str]) -> list[dict]:
    """Разбирает строки журнала, пропуская пустые и негодные."""
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records


def average_by_city(records: list[dict]) -> dict:
    """Средняя температура по каждому городу, округлённая до десятых."""
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0.0) + rec["temp"]
        count[city] = count.get(city, 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}


def warmest_city(records: list[dict]) -> str:
    """Город с наибольшей средней температурой.

    При равенстве — первый по алфавиту.
    """
    averages = average_by_city(records)
    return sorted(averages, key=lambda c: (-averages[c], c))[0]