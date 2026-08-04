item_name = input("Enter the name of the item: ")
price = float(input("Enter the price of the item: "))

quantity = 3
tax_rate = 0.06

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Item Name:", item_name)
print("Price:", price)
print("Quantity:", quantity)
print("Subtotal:RM", subtotal)
print("Tax: RM", tax)
print("Total Cost: RM", total)