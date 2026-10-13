"""
Assignment 3 - Functions (nested / inner functions)

Challenge 1: POS Receipt Generator   -> create_receipt_line(item_name, price)
Challenge 2: Movie Ticket Booking    -> book_ticket(movie_name, base_price, age)
"""

DISCOUNT_RATE = 0.15      # 15 % membership discount
TAX_RATE = 0.07           # 7 % sales tax
IS_3D = True              # 3D / IMAX upgrade switch
UPGRADE_CHARGE = 5.00


def create_receipt_line(item_name, price):
    def apply_discount(current_price):
        return current_price - current_price * DISCOUNT_RATE

    def apply_tax(current_price):
        return current_price + current_price * TAX_RATE

    final_total = apply_tax(apply_discount(price))
    print(f"Receipt: {item_name} | total_price: {final_total}")


def book_ticket(movie_name, base_price, age):
    def get_age_multiplier(age):
        if age < 12:
            return 0.5      # children: 50 % discount
        if age >= 65:
            return 0.7      # seniors: 30 % discount
        return 1.0

    def add_experience_upgrades(current_price):
        return current_price + UPGRADE_CHARGE if IS_3D else current_price

    final_total = add_experience_upgrades(base_price * get_age_multiplier(age))
    print(f"{movie_name}: | Total_Price: ${final_total}")


RUN_RECEIPT_DEMO = False      # challenge 1 was not part of the printed output

if __name__ == "__main__":
    if RUN_RECEIPT_DEMO:
        create_receipt_line("Leather Boots", 120.00)
        create_receipt_line("Gaming Laptop", 1500.00)

    book_ticket("Avatar 3", 14.00, 10)
    book_ticket("The Avengers", 14.00, 28)
