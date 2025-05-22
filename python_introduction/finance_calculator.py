Monthly_income = int(input("Enter your monthly income: "))
Total_monthly_expenses = int(input("Enter your total monthly expenses: "))

Monthly_savings = Monthly_income - Total_monthly_expenses

Annual_interest = 0.05
Projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)

print(f"Your monthly savings are: {Monthly_savings}")
print(f"Your projected savings after one year, with interest, is: {Projected_savings}")