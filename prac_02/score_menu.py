def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    while True:
        try:
            score = int(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score! Must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def determine_result(score):
    """Determine the result based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print stars equal to the score."""
    print("*" * score)


def display_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def main():
    """Main function to run the menu system."""
    score = get_valid_score()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip().upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Result: {determine_result(score)}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
