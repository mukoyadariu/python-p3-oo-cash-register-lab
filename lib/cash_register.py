class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.item_prices = []  # Initialize the list to store item prices

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.item_prices.extend([price] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.item_prices.pop()
            self.total -= last_item_price
            self.items.pop()

if __name__ == "__main__":
    register = CashRegister(20)
    register.add_item("macbook air", 1000)
    register.apply_discount()
    print(register.total)
    register.void_last_transaction()
    print(register.total)

