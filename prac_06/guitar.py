"""CP1404/CP5632 Practical - Guitar class.
EST TIME: 25 mins
REAL TIME: 22 mins

"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name, year, cost):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the guitar is in years."""
        return 2025 - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50


