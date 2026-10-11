# Jacob Van Dyke
# Portfolio Project


class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name.lower() == item_name.lower():
                self.cart_items.remove(item)
                return

        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name.lower() == modified_item.item_name.lower():
                item.item_quantity = modified_item.item_quantity
                return

        print("Item not found in cart. Nothing modified.")

    def get_num_items(self):
        item_count = 0
        for item in self.cart_items:
            item_count += item.item_quantity
        return item_count

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            item_cost = item.item_price * item.item_quantity
            total_cost += item_cost
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items()}")
        print()
        for item in self.cart_items:
            item.print_item_cost()
        print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print("CART DESCRIPTIONS:")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    user_input = input("Choose an option: ").lower()

    if user_input == "a":
        item_name = input("Enter the item name: ")
        item_description = input("Enter the item description: ")
        item_price = float(input("Enter the item price: "))
        item_quantity = int(input("Enter the item quantity: "))
        new_item = ItemToPurchase(
            item_name, item_price, item_quantity, item_description
        )
        cart.add_item(new_item)
    elif user_input == "r":
        cart.remove_item(input("Enter the name of the item to remove: "))
    elif user_input == "c":
        item_name = input("Enter the item name: ")
        item_quantity = int(input("Enter the new quantity: "))
        cart.modify_item(ItemToPurchase(item_name, item_quantity=item_quantity))
    elif user_input == "i":
        cart.print_descriptions()
    elif user_input == "o":
        cart.print_total()
    elif user_input == "q":
        print("Goodbye!")
        return False
    else:
        print("Invalid option. Please try again.")

    return True


def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    customer_shopping_cart = ShoppingCart(customer_name, current_date)

    continue_program = True
    while continue_program:
        continue_program = print_menu(customer_shopping_cart)


if __name__ == "__main__":
    main()
