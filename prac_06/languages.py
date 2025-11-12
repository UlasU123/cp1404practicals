"""CP1404/CP5632 Practical - Using the ProgrammingLanguage class.
EST TIME: 20 mins
REAL TIME: 18

"""

from programming_language import ProgrammingLanguage


def main():
    """Create ProgrammingLanguage objects and display their details."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]

    print("All languages:")
    for language in languages:
        print(language)

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()
