class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar."""
        return 2024 - self.year  # Assuming the current year is 2024

    def is_vintage(self):
        """Check if the guitar is vintage (50 or more years old)."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Define less-than comparison for sorting Guitars by year."""
        return self.year < other.year