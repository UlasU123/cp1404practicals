"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read data from file and display subject details."""
    subject_data = load_subject_data(FILENAME)
    display_subject_details(subject_data)


def load_subject_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])  # Convert number of students to int
            subject_data.append(parts)
    return subject_data


def display_subject_details(subject_data):
    """Display subject details neatly formatted."""
    for subject_code, lecturer, student_count in subject_data:
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")


main()

