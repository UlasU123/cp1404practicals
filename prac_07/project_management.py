"""
CP1404 Practical
Program for managing projects loaded from a text file.
EST TIME: 30 mins
REAL TIME: 113 mins
"""

from project import Project

FILENAME = "projects.txt"


def main():
    projects = load_projects(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    choice = get_menu_choice()
    while choice != "Q":
        if choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "S":
            save_projects(projects, FILENAME)
        else:
            print("Invalid choice")
        choice = get_menu_choice()

    print("Thank you for using project management!")


def get_menu_choice():
    """Display menu and get valid user choice."""
    print("\nMenu:")
    print("(D)isplay projects")
    print("(F)ilter projects by date")
    print("(A)dd new project")
    print("(U)pdate project")
    print("(S)ave projects")
    print("(Q)uit")
    return input(">>> ").upper()


def load_projects(filename):
    """Load projects from the given file."""
    projects = []
    in_file = open(filename, "r")
    in_file.readline()  # skip header
    for line in in_file:
        parts = line.strip().split("\t")
        name = parts[0]
        start_date = parts[1]
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        completion_percentage = int(parts[4])
        project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(project)
    in_file.close()
    return projects


def display_projects(projects):
    """Display incomplete and complete projects separately."""
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(f"  {project}")
    print("Completed projects:")
    for project in projects:
        if project.is_complete():
            print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects starting after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    print(f"Projects starting after {date_string}:")
    for project in projects:
        if project.start_date > date_string:
            print(f"  {project}")


def add_new_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Completion percentage: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_completion = input("New completion percentage (leave blank to skip): ")
    new_priority = input("New priority (leave blank to skip): ")
    if new_completion != "":
        project.update(completion=int(new_completion))
    if new_priority != "":
        project.update(priority=int(new_priority))


def save_projects(projects, filename):
    """Save all projects back to the file."""
    out_file = open(filename, "w")
    out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project in projects:
        print(f"{project.name}\t{project.start_date}\t{project.priority}\t"
              f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)
    out_file.close()
    print(f"{len(projects)} projects saved to {filename}")


main()

