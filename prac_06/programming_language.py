"""CP1404/CP5632 Practical - ProgrammingLanguage class
EST TIME: 20 mins
REAL TIME: 27 mins

"""

class ProgrammingLanguage:
    """Represent a programming language with its attributes."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a nicely formatted string representation of the object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"


