# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.

Coffee_total = 3.50 * 2
Muffin_total = 2.10 * 3
Water_total = 1.05 * 4
subtotal = Coffee_total + Muffin_total + Water_total
tax = subtotal * 0.06
total = subtotal + tax

print(
"========== RECEIPT ==========\n"
f"item\tprice\tqty\ttotal\n",
f"Coffee\t$3.50\t2\t${Coffee_total}\n",
f"Muffin\t$2.10\t3\t${Muffin_total}\n",
f"Water\t$1.50\t4\t${Water_total}\n",  
f"Subtotal\t\t\t${subtotal}\n",
f"Tax(6%)\t\t\t${tax}\n",
f"Total\t\t\t${total}\n"
)