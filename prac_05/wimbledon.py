"""
Wimbledon
Estimate: 25 minutes
Actual: 42 minutes
"""



FILENAME = "wimbledon.csv"


def main():
    records = load_data(FILENAME)
    champions, countries = extract_stats(records)

    print("Wimbledon Champions:")
    for name, count in champions.items():
        print(f"{name} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_data(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header line
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def extract_stats(records):
    champions = {}
    countries = set()
    for record in records:
        country = record[1]
        champion = record[2]
        countries.add(country)
        champions[champion] = champions.get(champion, 0) + 1
    return champions, countries


main()


