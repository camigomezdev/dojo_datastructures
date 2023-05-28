"""
A module for utils in the reports package.
"""
import logging

logger: logging.Logger = logging.getLogger(__name__)


def print_menu() -> None:
    """
    Prints the menu
    :return: None
    :rtype: NoneType
    """
    print("Select a report to generate:")
    print("1. City Report")
    print("2. Country Report")
    print("3. Age Report")
    print("4. Cities Report")
    print("5. Career Average Report")
    print("6. Above/Below Average Report")
    print("7. Age Group Report")
    print("8. Most Career City Report")
    print("0. Exit")


def get_user_choice_from_submenu(prompt: str, values: list[str]) -> str:
    """
    Prints a submenu with the given prompt and values, and returns the
     user's selection.
    :param prompt: The prompt to display
    :type prompt: str
    :param values: The values to display in the submenu
    :type values: list[str]
    :return: The user's selection
    :rtype: str
    """
    while True:
        print(prompt)
        for i, value in enumerate(values, start=1):
            print(f"{i}. {value}")
        print("0. Back")
        choice: str = input("Enter your choice: ")
        if choice.isdigit() and 0 <= int(choice) <= len(values):
            return choice
        logger.error("Invalid choice %s. Please try again.\n", choice)
