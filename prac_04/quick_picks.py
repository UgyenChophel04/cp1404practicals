import random

# Constants
NUMBERS_RANGE = 45  # The range for quick pick numbers (1 to 45)
NUMBERS_IN_PICK = 6  # The number of numbers in each quick pick


def generate_quick_pick():
    """Generates a list of 6 unique random numbers between 1 and 45."""
    quick_pick = []

    while len(quick_pick) < NUMBERS_IN_PICK:
        num = random.randint(1, NUMBERS_RANGE)
        if num not in quick_pick:
            quick_pick.append(num)

    quick_pick.sort()  # Sort the numbers in ascending order
    return quick_pick


def main():
    """Main function to generate and display quick picks."""
    num_picks = int(input("How many quick picks? "))  # Get the number of quick picks from the user

    for _ in range(num_picks):
        quick_pick = generate_quick_pick()

        # Print the quick pick numbers in a formatted way
        print(" ".join(f"{num:2}" for num in quick_pick))


if __name__ == "__main__":
    main()
