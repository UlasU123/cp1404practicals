"""
CP1404 Practical
Read guitar data from a file and display it
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitars from a file and display information."""
    guitars = load_guitars(FILENAME)

    # Sort guitars by year using a simple nested loop (no lambda)
    for i in range(len(guitars) - 1):
        for j in range(i + 1, len(guitars)):
            if guitars[j].year < guitars[i].year:
                guitars[i], guitars[j] = guitars[j], guitars[i]

    print("These are my guitars:")
    for guitar in guitars:
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"{guitar.name:30} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    in_file = open(filename, "r")
    for line in in_file:
        parts = line.strip().split(",")
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()
    return guitars


main()



