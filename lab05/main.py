import logstats


def main():
    path = input().strip()

    with open(path, encoding="utf-8") as log:
        counts = logstats.count_levels(log)

    total = sum(counts.values())
    errors_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    print(total)
    print(errors_count)
    print(broken_count)

    with open(path, encoding="utf-8") as log:
        errors = logstats.top_errors(log, 3)

    report = logstats.format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as out:
        out.write(report)


if __name__ == "__main__":
    main()
