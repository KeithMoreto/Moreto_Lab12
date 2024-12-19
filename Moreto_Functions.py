def display_menu(menu):
    """Display the food menu with prices."""
    print("Menu:")
    for item, price in menu:
        print(f"{item}: ${price:.2f}")
    print()  

def get_order(menu):
    """Get the user's order from the menu."""
    while True:
        choice = input("Please enter the name of the item you want to order: ").strip()
        for item, price in menu:
            if item.lower() == choice.lower():  
                return item, price
        print("Invalid item. Please choose from the menu.")

def process_payment(total):
    """Process the payment and ensure sufficient cash is provided."""
    while True:
        try:
            cash_rendered = float(input(f"Total cost is ₱{total:.2f}. Please enter the cash rendered: ₱"))
            if cash_rendered >= total:
                return cash_rendered
            else:
                print(f"Insufficient cash. You need to provide at least ₱{total:.2f}.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def calculate_change(cash_rendered, total):
    """Calculate the change to be returned to the customer."""
    return cash_rendered - total

def main():
    """Main function to run the food ordering system."""
    menu = [
        ("Burger", 50.00),
        ("Pizza", 200.00),
        ("Salad", 30.00),
        ("Soda", 20.00),
        ("Fries", 30.00)
    ]

    display_menu(menu)
    
    item, price = get_order(menu)
    print(f"You have selected: {item} - ₱{price:.2f}")

    total = price
    cash_rendered = process_payment(total)
    
    change = calculate_change(cash_rendered, total)
    print(f"Thank you for your order! Your change is: ₱{change:.2f}")

# Directly call the main function
main()