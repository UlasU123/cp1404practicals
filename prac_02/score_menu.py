import random


def main():
    score = get_valid_score()
    choice = get_menu_choice()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_result(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        choice = get_menu_choice()
    print("Farewell")


def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score


def get_menu_choice():
    menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)
    return input(">>> ").upper()


def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()


