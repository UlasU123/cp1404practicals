"""
CP1404 Practical
Project class to represent a project with name, start date, priority, cost estimate, and completion percentage.
EST TIME: 30 mins
REAL TIME: 27 mins
"""


class Project:
    """Represent a project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of the Project."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.completion_percentage == 100

    def update(self, completion=None, priority=None):
        """Update completion percentage or priority if provided."""
        if completion is not None:
            self.completion_percentage = completion
        if priority is not None:
            self.priority = priority

