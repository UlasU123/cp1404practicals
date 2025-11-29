"""
CP1404 Practical
UnreliableCar test program
"""

from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    # create an unreliable car with 50% reliability
    car = UnreliableCar("Untrustworthy", 100, 50)

    # try several drives
    for i in range(1, 6):
        distance = 20
        actual_driven = car.drive(distance)
        print(f"Attempt {i}: tried to drive {distance}km, actually drove {actual_driven}km")

    print(car)


main()
