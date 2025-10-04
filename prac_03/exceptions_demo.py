
"""
a ValueError occurs if the user enters something that is not a valid integer e.g. "abc" or "3.5".

ZeroDivisionError occurs if the denominator entered is 0.

yes by using a loop to repeatedly ask for the denominator until it is not zero.
"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

