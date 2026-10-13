"""Модуль обработки записей метеостанции."""


def parse_record(line: str) -> dict:
    """Разбирает строку «город;температура;дата» в словарь."""
    parts = line.split(";")
    city, temp, date = parts
    return {"city": city, "temp": float(temp), "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    """Разбирает строки журнала, пропуская пустые."""
    records = []
    for line in lines:
        if not line.strip():
            continue
        records.append(parse_record(line))
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