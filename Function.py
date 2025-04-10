# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Call the function and display the result
    final_price = calculate_discount(original_price, discount)

    if final_price < original_price:
        print(f"Discount applied! Final price: ₦{final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: ₦{original_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
