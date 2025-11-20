"""
CP1404 Practical
Taxi test program
"""

from taxi import Taxi


def main():
    """Test the Taxi class."""
    # create a taxi
    taxi = Taxi("Prius 1", 100)

    # drive the taxi
    taxi.drive(40)
    print(taxi)
    print(f"Fare: ${taxi.get_fare():.2f}")

    # start a new fare and drive again
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print(f"Fare: ${taxi.get_fare():.2f}")


main()
