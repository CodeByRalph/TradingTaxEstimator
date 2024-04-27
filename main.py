

taxable_amount = float(input("Enter amount of trading profit: "))
tax_bracket = int(input("what is your income tax rate: "))

long_term_capital_gains = (taxable_amount * .60) * .15
short_term_capital_gains = (taxable_amount * .40) * (tax_bracket / 100)

owed = long_term_capital_gains + short_term_capital_gains

print(f"You owe: {owed}")
print(f"Your profit: {taxable_amount - owed}")

