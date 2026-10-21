import sys
from logstats import count_levels, top_errors, format_report


def main():
    filename = input().strip()
    with open(filename, encoding="utf-8") as f:
        counts = count_levels(f)

    with open(filename, encoding="utf-8") as f:
        errors = top_errors(f, 3)

    total_parsed = sum(counts.values())
    total_errors = counts.get("ERROR", 0)
    total_broken = counts.get("BROKEN", 0)

    print(total_parsed)
    print(total_errors)
    print(total_broken)

    report_text = format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as out:
        out.write(report_text)


if __name__ == "__main__":
    main()