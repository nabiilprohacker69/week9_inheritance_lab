"""Console menu."""
import os
from inventory import Inventory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

DATA_FILE = "inventory.json"


def ask_number(prompt, number_type):
    while True:
        try:
            return number_type(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def data_representation(inventory):
    print("==================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("==================================================\n")
    if os.path.exists(DATA_FILE):
        print("inventory.json found")
        try:
            inventory.load(DATA_FILE)
            print("Inventory loaded successfully.\n")
        except (ValueError, KeyError) as error:
            print(f"Could not load inventory: {error}\n")
    else:
        print("inventory.json not found. Starting with an empty inventory.\n")


def print_menu():
    print("--------------MENU---------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------------\n")


def option_1(inventory):
    inventory.display_all()
    print()


def option_2(inventory):
    print("Add New Product")
    kind = input("Product type - (p)hysical or (d)igital: ").strip().lower()
    if kind not in ("p", "d"):
        print("Invalid product type.\n")
        return
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    product_price = ask_number("Price: ", lambda text: float(text.replace("$", "")))
    product_stock = ask_number("Stock Quantity: ", int)
    if kind == "p":
        weight = ask_number("Weight (kg): ", float)
        product = PhysicalProduct(product_id, product_name, product_price, product_stock, weight)
    else:
        size = ask_number("Download size (MB): ", float)
        product = DigitalProduct(product_id, product_name, product_price, product_stock, size)
    try:
        inventory.add_product(product)
        print("Product added successfully.\n")
    except ValueError as error:
        print(f"{error}\n")


def option_3(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.get_product(product_id)
    if product is None:
        print("Product ID not found.\n")
        return
    print("\nProduct Found")
    print(f"Name: {product.name}\nStock: {product.stock}\n")
    new_quantity = ask_number("New stock quantity: ", int)
    try:
        inventory.update_stock(product_id, new_quantity)
        print("Stock updated successfully!\n")
    except ValueError as error:
        print(f"{error}\n")


def option_4(inventory):
    print("Search Product")
    product = inventory.get_product(input("Enter Product ID: "))
    if product is None:
        print("Product ID not found.\n")
        return
    print("\nProduct Found")
    print("---------------------------------")
    product.display_information()
    print(f"   Fulfilment: {product.get_fulfilment_info()}")
    if hasattr(product, "calculate_shipping_cost"):          # only shippable products
        print(f"   Shipping cost: ${product.calculate_shipping_cost():.2f}")
    print("---------------------------------\n")


def option_5(inventory):
    print("Saving Inventory...")
    inventory.save(DATA_FILE)
    print("Inventory saved successfully.\n")


def main():
    inventory = Inventory()
    data_representation(inventory)
    print_menu()
    actions = {"1": option_1, "2": option_2, "3": option_3, "4": option_4, "5": option_5}
    while True:
        choice = input("Enter Option: ").strip()
        if choice in actions:
            actions[choice](inventory)
        elif choice == "6":
            if input("Save before exit? (y/n): ").strip().lower() == "y":
                option_5(inventory)
            print("Thank you for using Inventory Management System.\nProgram terminated.")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()