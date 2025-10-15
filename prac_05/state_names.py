"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""



CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "SA": "South Australia",
    "TAS": "Tasmania",
    "VIC": "Victoria",
    "ACT": "Australian Capital Territory"
}

print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()


