"""
===============================================================================
 Shopping List Dictionary Practice
===============================================================================

Objective:
    Create a dictionary to represent a shopping list, practice adding,
    accessing, and modifying key-value pairs.

Features:
    - Create an empty dictionary to start.
    - Add five grocery items with their specified quantities:
        • apples, Qty: 4
        • bananas, Qty: 6
        • milk, Qty: 2
        • bread, Qty: 1
        • eggs, Qty: 12
    - Access and print the quantity of apples.
    - Update the quantity of milk.
    - Remove bananas from the shopping list.
    - Combine all steps into a single program and run it.

-------------------------------------------------------------------------------
 Author: Marcos Antonio de Castilho Junior
 Created: 2025-04-28
 Python Version: 3.12
===============================================================================
"""

shopping_list = {}

# Add items to the shopping list
shopping_list["apples"] = 4
shopping_list["bananas"] = 6
shopping_list["milk"] = 2
shopping_list["bread"] = 1
shopping_list["eggs"] = 12

# Print quantity of apples
print(f"Quantity of apples: {shopping_list['apples']}")

# Update quantity of milk
shopping_list["milk"] = 3
print(f"Updated milk quantity: {shopping_list['milk']}")

# Remove bananas from the list
del shopping_list["bananas"]
print(f"Final shopping list: {shopping_list}")
