


COLOUR_NAMES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "BlueViolet": "#8a2be2"
}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    if colour_name in COLOUR_NAMES:
        print(f"{colour_name} is {COLOUR_NAMES[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ")



