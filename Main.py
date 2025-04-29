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

def parse_input_to_items(user_input):
    """
    Processes and formats a raw string of items entered by the user.

    This function was created to centralize and simplify the repeated logic
    of cleaning and formatting user input across multiple features of the app.
    Previously, the same input treatment logic (e.g., replacing commas, splitting,
    trimming spaces, and capitalizing) appeared in multiple functions such as
    add_item_to_list, remove_from_list, and update_item.

    Features
    ========
    - Replaces commas with spaces to standardize separators.
    - it Splits the input string into a list of individual item strings.
    - Removes extra whitespace and applies the title case to each item.

    Parameters
    ==========
    user_input : str
        The raw input string from the user, containing item names.

    Returns
    =======
    list
        A list of cleaned and formatted item strings.
    """
    # Replace commas with spaces to unify how items are separated
    cleaned_input = user_input.replace(",", " ")

    # Split the cleaned input into a list of words (each assumed to be an item)
    raw_items = cleaned_input.split()

    # Prepare a new list to hold the formatted items
    formatted_items = []

    # Loop through each raw item string
    for item in raw_items:
        # Remove any leading/trailing whitespace and capitalize the first letter
        formatted_item = item.strip().title()

        # Add the cleaned item to the new list
        formatted_items.append(formatted_item)

    # Return the list of formatted item names to be used elsewhere
    return formatted_items


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
        print("\n Your shopping list:")
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
    items = parse_input_to_items(new_items)
    for item in items:
        item_to_verify = item
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
    items = parse_input_to_items(items_to_remove)
    for item in items:
        formatted_item = item
        if formatted_item in shopping_list:
            del shopping_list[formatted_item]
            time.sleep(DELAY)
            print(f"{formatted_item} removed from shopping list.")
        else:
            time.sleep(DELAY)
            print(f"{formatted_item} is not in your shopping list.")
    return shopping_list


def update_item(shopping_list):
    """
    Prompts the user to update the quantity of one or more existing items in the shopping list.

    Features
    ========
    - Displays the current shopping list before asking for input.
    - Accepts multiple items separated by commas or spaces.
    - Validates if the item exists in the list before updating.
    - Allows setting a positive quantity or marking as "Quantity not specified" if the quantity is zero.
    - Handles invalid inputs gracefully by prompting the user again.

    Returns
    =======
    dict
        The updated shopping list with modified quantities for the selected items.
    """
    show_list(shopping_list)
    items_to_update = input("Please enter item/items to update, or press enter to cancel: ")
    if items_to_update == "":
        return shopping_list
    items = parse_input_to_items(items_to_update)
    for item in items:
        formatted_item = item
        if formatted_item not in shopping_list:
            print(f"{formatted_item} is not in your shopping list.")
            continue
        while True:
            try:
                quantity = int(input(f"Enter quantity for {formatted_item}: "))
                if quantity < 0:
                    print("Quantity must be a positive number.")
                    continue
                elif quantity == 0:
                    print(f"No quantity specified for {formatted_item}.")
                    shopping_list[formatted_item] = "Quantity not specified"
                    break
                else:
                    shopping_list[formatted_item] = quantity
                    print(f"{formatted_item} updated. Quantity: {quantity}.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
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
    print("Enter '4' to update an item's quantity.\n")
    print("Enter '5' to quit the application.\n")


# Runs the app only if this file is executed directly, not when imported.
if __name__ == "__main__":
    welcome_message()
    # Starts an infinite loop to keep showing the menu until the user decides to quit.
    while True:
        menu()
        choice = input()
        menu_actions = {
            "1": show_list,
            "2": add_item_to_list,
            "3": remove_from_list,
            "4": update_item,
            "5": None # Option 5 is set to None because it doesn't call a function; the program handles it manually with break.
        }
        if choice == "5":
            break
        elif choice in menu_actions:
            # We access the corresponding function from the dictionary using the user's choice as the key.
            # Then we immediately call the function by adding parentheses and pass user_list as an argument.
            # Example: if choice == "2", this runs add_item_to_list(user_list)
            menu_actions[choice](user_list)
        else:
            time.sleep(DELAY)
            print("Invalid choice. Please try again and use a number between 1 and 5.")
