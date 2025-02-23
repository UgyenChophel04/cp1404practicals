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
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

print(CODE_TO_NAME)

# Convert input to uppercase to ensure consistency
state_code = input("Enter short state: ").upper()

# Loop to continuously ask for state codes
while state_code != "":
    try:
        # Fetch the full state name using the state code
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        # Handle invalid state code input
        print("Invalid short state")

    state_code = input("Enter short state: ").upper()

# Print all states and their names
print("\nAll states:")
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")
