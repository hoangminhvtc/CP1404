COLOR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "7fffd4", "aquamarine2": "76eec6", "aquamarine4": "458b74", "azure1": "f0ffff", "azure2": "e0eeee", "azure3": "c1cdcd"}
color = input("Enter color name: ")
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("Invalid color name")
    state = input("Enter short state: ")
