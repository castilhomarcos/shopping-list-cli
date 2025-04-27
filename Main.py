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
 Updated: 2025-04-29
 Python Version: 3.12
===============================================================================
"""

import time


user_list = {}
DELAY = 1




def show_list(shopping_list):
    """
    Displays the current shopping list.

    Features
    ========
    - Shows a message if the shopping list is empty.
    - Otherwise, prints each item with its quantity.

    Parameters
    ==========
    shopping_list : dict
        The shopping list to display, where the key is the item name and the value is the quantity.

    Returns
    =======
    None
    """
    if not shopping_list:
        time.sleep(DELAY)
        print("Your shopping list is empty.")
    else:
        print("\n🛒 Your shopping list:")
        for item, value in shopping_list.items():
            print(f"•Item: {item} - Quantity: {value} ")




def add_item_to_list(shopping_list):
    """
    Prompts the user to add one or more items to the shopping list with specified quantities.

    Features
    ========
    - Accepts multiple items separated by commas or spaces.
    - Asks for a quantity for each new item.
    - Validates the quantity (must be a positive integer).
    - Allows the user to skip specifying a quantity (marks as "Quantity not specified").

    Returns
    =======
    dict
        The updated shopping list with new items added.

    Examples
    ========
    Example 1:
    User inputs: apples, bananas
    Then inputs: 4 for apples, 6 for bananas.

    Example 2:
    User inputs: bread
    Then inputs: 0 (quantity not specified).

    Example 3:
    User inputs an invalid quantity like "two"
    Prompted again until a valid number is entered.
    """
    new_items = input("Please enter new item(s) to add (separated by comma or space): ")
    # Prompts the user to input items separated by commas or spaces.
    if new_items == "":
        return shopping_list
    cleaned_input = new_items.replace(",", " ")
    # Replaces commas with spaces to standardize separation.
    items = cleaned_input.split()
    # Splits the input string into a list of items using spaces as separators.
    for item in items:
        item_to_verify = item.strip().title()
        if item_to_verify in user_list:
            print(f"{item_to_verify} is already in your shopping list.")
        else:
            while True:
                try:
                    quantity = int(input(f"Enter quantity for {item_to_verify}: "))
                    if quantity < 0:
                        print("Quantity must be a positive number.")
                        continue
                    elif quantity == 0:
                        print(f"No quantity specified for {item_to_verify}. It has been added to your list.")
                        shopping_list[item_to_verify] = "Quantity not specified"
                        break
                    else:
                        shopping_list[item_to_verify] = quantity
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
    return shopping_list





def remove_from_list(shopping_list):
    """
    Prompts the user to remove one or more items from the shopping list.

    Accepts items separated by commas or spaces. If an item is not found, it informs the user but continues.

    Example:
        Input: "apples, bananas"
        Removes: any matching items currently in the list

    Returns
    =======
    dict
        The updated shopping list with specified items removed.
    """
    items_to_remove = input("Please enter item(s) to remove (separated by comma or space), or press enter to cancel: ")
    if items_to_remove == "":
        return shopping_list
    cleaned_input = items_to_remove.replace(",", " ")
    items = cleaned_input.split()
    for item in items:
        formatted_item = item.strip().title()
        if formatted_item in shopping_list:
            del shopping_list[formatted_item]
            time.sleep(DELAY)
            print(f"{formatted_item} removed from shopping list.")
        else:
            time.sleep(DELAY)
            print(f"{formatted_item} is not in your shopping list.")
    return shopping_list


def welcome_message():
    """
    Displays the initial welcome message when the application starts.

    Returns
    =======
    None
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

    Returns
    =======
    None
    """
    print("Enter '1' to list your current shopping list.\n")
    print("Enter '2' to add an item to your shopping list.\n")
    print("Enter '3' to remove an item from your shopping list.\n")
    print("Enter '4' to quit the application.\n")



if __name__ == "__main__":
    welcome_message()

    while True:
        menu()
        choice = input()
        if choice == "1":
            show_list(user_list)
        elif choice == "2":
            user_list = add_item_to_list(user_list)
        elif choice == "3":
            user_list = remove_from_list(user_list)
        elif choice == "4":
            print("Thank you for using your shopping list app!")
            break
        else:
            time.sleep(DELAY)
            print("Invalid choice. Please try again and use a number between 1 and 4.")
