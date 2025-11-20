"""
CP1404 Practical
Silver Service Taxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness factor and flagfall."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = 1.23 * fanciness
        self.current_fare_distance = 0

    def get_fare(self):
        """Return fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string showing fanciness and flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
