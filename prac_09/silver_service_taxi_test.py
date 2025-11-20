"""
CP1404  Practical
Silver Service Taxi test program
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class."""
    taxi = SilverServiceTaxi("Limo", 100, 2)

    taxi.drive(18)
    fare = taxi.get_fare()

    print(f"Taxi drove 18km, fare = ${fare:.2f}")
    print(taxi)


main()
