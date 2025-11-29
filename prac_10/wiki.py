"""
Program to get a Wikipedia page summary.
"""

import wikipedia


def main():
    title = input("Enter page title: ")

    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(f"\nTitle: {page.title}")
        print(f"Summary:\n{page.summary}")

    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation Error. Options include:")
        for option in e.options:
            print(option)

    except wikipedia.exceptions.PageError:
        print("Page not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
