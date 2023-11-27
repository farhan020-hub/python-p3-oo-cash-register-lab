#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Format the total to remove .00 if the total is a whole number
            formatted_total = f"{self.total:.2f}".rstrip('0').rstrip('.') if '.' in f"{self.total:.2f}" else f"{self.total:.0f}"
            print(f"After the discount, the total comes to ${formatted_total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        if self.total < 0:
            self.total = 0
