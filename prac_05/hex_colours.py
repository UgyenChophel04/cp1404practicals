"""
Color Code Lookup Program
Estimate: 15 minutes
Actual:   12 minutes
"""

# Constant dictionary of color names and their hexadecimal codes
COLOR_CODES = {
    "absolute zero": "#0048ba",
    "acid green": "#b0bf1a",
    "aliceblue": "#f0f8ff",
    "alizarin crimson": "#e32636",
    "amethyst": "#9966cc",
    "antique white": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc"
}

# Loop to allow the user to enter color names
color_name = input("Enter a color name (or press Enter to stop): ").lower()

while color_name != "":
    if color_name in COLOR_CODES:
        print(f"The hexadecimal code for {color_name.capitalize()} is {COLOR_CODES[color_name]}")
    else:
        print("Invalid color name. Please try again.")

    color_name = input("Enter a color name (or press Enter to stop): ").lower()

print("Goodbye!")
