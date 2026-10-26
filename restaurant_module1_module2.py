# Restaurant Food Ordering and Sales System
# Module 1: Menu Management
# Module 2: Order and Billing

class FoodItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = float(price)
        self.category = category

    def calculate_price(self):
        return self.price

    def display(self):
        print(f"{self.name:<20} {self.category:<15} Rs. {self.calculate_price():.2f}")


class MainCourse(FoodItem):
    def calculate_price(self):
        return self.price


class Beverage(FoodItem):
    def calculate_price(self):
        return self.price


class Dessert(FoodItem):
    def calculate_price(self):
        return self.price


# ---------------- MODULE 1: MENU MANAGEMENT ----------------

menu = {
    "Veg Burger": MainCourse("Veg Burger", 120, "Main Course"),
    "Pizza": MainCourse("Pizza", 250, "Main Course"),
    "Pasta": MainCourse("Pasta", 180, "Main Course"),
    "Cold Coffee": Beverage("Cold Coffee", 90, "Beverage"),
    "Lemonade": Beverage("Lemonade", 50, "Beverage"),
    "Ice Cream": Dessert("Ice Cream", 70, "Dessert"),
    "Brownie": Dessert("Brownie", 100, "Dessert")
}

categories = {"Main Course", "Beverage", "Dessert"}


def display_menu():
    print("\n" + "=" * 55)
    print("              RESTAURANT MENU")
    print("=" * 55)
    print(f"{'Item':<20} {'Category':<15} Price")
    print("-" * 55)

    for item in menu.values():
        item.display()

    print("=" * 55)


def add_menu_item():
    try:
        name = input("Enter new item name: ").strip()
        if not name:
            print("Item name cannot be empty.")
            return
        if name in menu:
            print("An item with this name already exists.")
            return

        print("Categories:", ", ".join(sorted(categories)))
        category = input("Enter category: ").strip().title()
        if category not in categories:
            print("Invalid category.")
            return

        price = float(input("Enter price (Rs.): "))
        if price <= 0:
            print("Price must be greater than zero.")
            return

        if category == "Main Course":
            item = MainCourse(name, price, category)
        elif category == "Beverage":
            item = Beverage(name, price, category)
        else:
            item = Dessert(name, price, category)

        menu[name] = item
        print(f"{name} added to the menu.")
    except ValueError:
        print("Invalid price. Please enter a number.")


# ---------------- MODULE 2: ORDER AND BILLING ----------------

def take_order():
    if not menu:
        print("The menu is empty.")
        return

    order = {}  # item name -> quantity

    while True:
        display_menu()
        choice = input("Enter item name to order (or 'done' to finish): ").strip()

        if choice.lower() == "done":
            break

        if choice not in menu:
            print("Item unavailable. Please choose an item shown on the menu.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Invalid quantity. Enter a whole number.")
            continue

        order[choice] = order.get(choice, 0) + quantity
        print(f"Added {quantity} x {choice} to your order.")

    if not order:
        print("No items were ordered.")
        return

    generate_bill(order)


def generate_bill(order):
    print("\n" + "=" * 55)
    print("                    CUSTOMER BILL")
    print("=" * 55)
    print(f"{'Item':<20} {'Qty':>5} {'Price':>10} {'Total':>12}")
    print("-" * 55)

    grand_total = 0.0

    for name, quantity in order.items():
        # Check that the item still exists in the menu
        if name not in menu:
            print(f"Skipping unavailable item: {name}")
            continue

        unit_price = menu[name].calculate_price()
        line_total = unit_price * quantity
        grand_total += line_total
        print(f"{name:<20} {quantity:>5} {unit_price:>10.2f} {line_total:>12.2f}")

    print("-" * 55)
    print(f"{'Grand Total (Rs.)':>40} {grand_total:>12.2f}")
    print("=" * 55)
    print("Thank you for visiting!")


# ---------------- MAIN PROGRAM ----------------

def main():
    while True:
        print("\n===== RESTAURANT SYSTEM =====")
        print("1. Display Menu")
        print("2. Add Menu Item")
        print("3. Place Order and Generate Bill")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            display_menu()
        elif choice == "2":
            add_menu_item()
        elif choice == "3":
            take_order()
        elif choice == "4":
            print("Exiting Restaurant System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
