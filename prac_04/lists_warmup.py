
numbers = [3, 1, 4, 1, 5, 9, 2]



# Predicted values before testing

# numbers[0] to 3
# numbers[-1] to 2
# numbers[3] to 1
# numbers[:-1] to [3, 1, 4, 1, 5, 9]
# numbers[3:4] to [1]
# 5 in numbers is True
# 7 in numbers is False
# "3" in numbers is False
# numbers + [6, 5, 3] to [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)





