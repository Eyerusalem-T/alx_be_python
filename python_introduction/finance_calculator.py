monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_interest_rate = 0.05
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Projected annual savings after including interest: ${projected_savings:.2f}")