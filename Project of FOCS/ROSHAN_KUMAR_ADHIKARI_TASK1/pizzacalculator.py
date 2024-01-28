# Constants
PIZZA_PRICE = 12.00
DELIVERY_CHARGE = 2.50
TUESDAY_DISCOUNT = 0.50
APP_DISCOUNT = 0.25

def get_positive_int(prompt):
    """Gets a positive integer from the user."""
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                raise ValueError
            return num
        except ValueError:
            print("Please enter a positive integer!")

def get_y_n(prompt):
    """Gets a yes/no answer from the user."""
    while True:
        answer = input(prompt).lower()
        if answer in ("y", "n"):
            return answer == "y"
        else:
            print("Please answer 'Y' or 'N'.")

def calculate_base_price(num_pizzas, is_tuesday):
    """Calculates the base price of the order, considering the number of pizzas and Tuesday discount."""
    base_price = num_pizzas * PIZZA_PRICE
    if is_tuesday:
        base_price *= (1 - TUESDAY_DISCOUNT)
    return base_price

def calculate_total_price(base_price, is_delivery, use_app):
    """Calculates the total price, considering delivery and app discounts."""
    if is_delivery:
        base_price += DELIVERY_CHARGE
    if use_app:
        base_price *= (1 - APP_DISCOUNT)
    return round(base_price, 2)

def print_welcome_message():
    """Prints a welcome message to the user."""
    print("BPP Pizza Price Calculator")
    print("=========================")

def main():
    """Gathers order details, calculates and displays the total price."""
    print_welcome_message()

    num_pizzas = get_positive_int("How many pizzas ordered? ")
    is_delivery = get_y_n("Is delivery required? ")
    is_tuesday = get_y_n("Is it Tuesday? ")
    use_app = get_y_n("Did the customer use the app? ")

    base_price = calculate_base_price(num_pizzas, is_tuesday)
    total_price = calculate_total_price(base_price, is_delivery, use_app)

    print(f"Total Price: £{total_price}.")

if __name__ == "__main__":
    main()
