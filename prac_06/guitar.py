"""CP1404/CP5632 Practical - Guitar class.
Estimate: 30 minutes
Actual: 35 minutes
"""

import datetime


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
        """Return the age of the guitar based on the current year."""
        current_year = datetime.datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Check if the guitar is 50 or more years old."""
        return self.get_age() >= 50