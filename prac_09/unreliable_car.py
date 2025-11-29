"""
CP1404 Practical
UnreliableCar class
"""

from random import randint
from prac_06.car import Car


class UnreliableCar(Car):
    """A Car that sometimes does not drive based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise the UnreliableCar with reliability percentage."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive.

        The car will only drive if a random number (0–100) is less than the reliability.
        Otherwise, it drives 0 km.
        """
        random_number = randint(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        return 0
