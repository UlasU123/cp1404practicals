"""CP1404/CP5632 Practical - Test for Guitar class.
EST TIME: 25 mins
REAL TIME: 28 mins

"""

from prac_06.guitar import Guitar


def main():
    """Test Guitar class functionality."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 900.00)

    print(f"{gibson.name} get_age() - Expected 103. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 12. Got {another_guitar.get_age()}")

    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


main()


