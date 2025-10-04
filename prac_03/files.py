
# Ask the user for their name and write it to a file
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# Read the name back from the file and display it
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# Read numbers from a file and process them
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# Sum all numbers in the file
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    total += int(line)
in_file.close()
print(f"The total of all numbers in numbers.txt is {total}")

