def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.
    """

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price

# qst 2. asking  the user for input
if __name__ == "__main__":
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(price, discount_percent)
        print(f"The final price after applying the discount is: {final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")
