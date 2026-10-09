import sys

from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)

    print(len(records))
    print(len(lines) - len(records) - sum(1 for line in lines if not line.strip()))

    if not records:
        print("Нет корректных записей")
        return

    averages = average_by_city(records)
    city = warmest_city(records)
    print(f"{averages[city]:.1f}")


if __name__ == "__main__":
    main()
