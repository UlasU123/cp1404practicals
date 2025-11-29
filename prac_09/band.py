"""
CP1404 Practical
Band class, using Musicians
"""

class Band:
    """Band class to manage a group of musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band and its members."""
        members = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({members})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their instrument."""
        results = []
        for musician in self.musicians:
            results.append(musician.play())
        return "\n".join(results)
