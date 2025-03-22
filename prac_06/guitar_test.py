"""CP1404/CP5632 Practical - Test code for Guitar class.
Estimate: 15 minutes
Actual: 10 minutes
"""

from guitar import Guitar


def main():
    """Test the Guitar class methods."""
    current_year = 2024  # Update this based on the current year when testing
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 0)

    # Test get_age()
    expected_age_gibson = current_year - 1922
    print(f"{gibson.name} get_age() - Expected {expected_age_gibson}. Got {gibson.get_age()}")
    expected_age_another = current_year - 2013
    print(f"{another.name} get_age() - Expected {expected_age_another}. Got {another.get_age()}")

    # Test is_vintage()
    print(f"{gibson.name} is_vintage() - Expected {expected_age_gibson >= 50}. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected {expected_age_another >= 50}. Got {another.is_vintage()}")


if __name__ == "__main__":
    main()