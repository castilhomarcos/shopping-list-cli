"""
===============================================================================
 Shopping List App
===============================================================================

A simple interactive shopping list application that allows users to view,
add, and remove items through a console-based menu system.

-------------------------------------------------------------------------------
 Features:
 - View the current shopping list
 - Add multiple items at once (avoiding duplicates)
 - Remove multiple items at once (ignoring missing items)
-------------------------------------------------------------------------------

Usage:
    Run this script and follow the on-screen prompts in the console.

-------------------------------------------------------------------------------
 Author: Marcos Antonio de Castilho Junior
 Created: 2025-04-26
 Python Version: 3.12
===============================================================================
"""

import time
import os


shopping_list = []
DELAY = 1


def clear_screen():
    """
    Clears the console screen based on the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def show_list():
    """
    Displays the current shopping list.

    If the list is empty, it notifies the user. Otherwise, it prints each item in the list.
    """
    if not shopping_list:
        time.sleep(DELAY)
        print("Your shopping list is empty.")
    else:
        print("\n🛒 Your shopping list:")
        for item in shopping_list:
            print(f"• {item}")
        print()


def add_to_list():
    """
    Prompts the user to add one or more items to the shopping list.

    Accepts items separated by commas or spaces. Duplicate entries are ignored.

    Example:
        Input: "apples, bananas oranges"
        Adds: ["Apples", "Bananas", "Oranges"]

    :return: None
    """
    new_items = input("Please enter new item(s) to add (separated by comma or space): ")
    if new_items == "":
        return
    cleaned_input = new_items.replace(",", " ")
    items = cleaned_input.split()
    for item in items:
        formatted_item = item.strip().title()
        if formatted_item in shopping_list:
            print(f"{formatted_item} is already in your shopping list.")
        else:
            shopping_list.append(formatted_item)
            time.sleep(DELAY)
            print(f"{formatted_item} added to shopping list.")


def remove_from_list():
    """
    Prompts the user to remove one or more items from the shopping list.

    Accepts items separated by commas or spaces. If an item is not found, it informs the user but continues.

    Example:
        Input: "apples, bananas"
        Removes: any matching items currently in the list

    :return: None
    """
    items_to_remove = input("Please enter item(s) to remove (separated by comma or space), or press enter to cancel: ")
    if items_to_remove == "":
        return
    cleaned_input = items_to_remove.replace(",", " ")
    items = cleaned_input.split()
    for item in items:
        formatted_item = item.strip().title()
        if formatted_item in shopping_list:
            shopping_list.remove(formatted_item)
            time.sleep(DELAY)
            print(f"{formatted_item} removed from shopping list.")
        else:
            time.sleep(DELAY)
            print(f"{formatted_item} is not in your shopping list.")


def welcome_message():
    """
    Displays the initial welcome message when the application starts.

    :return: None
    """
    print("Welcome to your shopping list app!")
    print("What would you like to do today?\n")


def menu():
    """
    Displays the main menu options for user interaction.

    This function prints the options available to the user:
    - 1: View current shopping list
    - 2: Add item(s) to the shopping list
    - 3: Remove item(s) from the shopping list
    - 4: Quit the application

    :return: None
    """
    print("Enter '1' to list your current shopping list.\n")
    print("Enter '2' to add an item to your shopping list.\n")
    print("Enter '3' to remove an item from your shopping list.\n")
    print("Enter '4' to quit the application.\n")



if __name__ == "__main__":
    welcome_message()

    while True:
        clear_screen()
        menu()
        choice = input()
        if choice == "1":
            show_list()
        elif choice == "2":
            add_to_list()
        elif choice == "3":
            remove_from_list()
        elif choice == "4":
            print("Thank you for using your shopping list app!")
            break
        else:
            time.sleep(DELAY)
            print("Invalid choice. Please try again.")
