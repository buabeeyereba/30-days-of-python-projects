
print('=' * 62)
print("LOAN ELIGIBILITY & REPAYMENT ESTIMATOR")
print('=' * 62)
print()


monthly_income = float(input("Your monthly income after tax (Naira): "))
existing_debt = float(input("Existing monthly debt payments (Naira): "))
loan_amount = float(input("Loan amount you want (Naira): "))
interest_rate = float(input("Annual interest rate in percent (e.g. 18): "))
loan_years = int(input("Loan term in years (e.g. 5): "))


loan_months = loan_years * 12
rate_per_month = interest_rate / 100 / 12
growth = (1 + rate_per_month) ** loan_months  
monthly_payment = loan_amount * rate_per_month * growth / (growth - 1)
total_repayment = monthly_payment * loan_months
total_interest = total_repayment - loan_amount   


debt_to_income = existing_debt / monthly_income
dti_ok = debt_to_income <= 0.36  
payment_ok = monthly_payment <= (monthly_income * 0.30) 
eligible = dti_ok and payment_ok


payment_display = round(monthly_payment, 2)
repayment_display = round(total_repayment, 2)
interest_display = round(total_interest, 2)

print()

print('-' * 60)
print(f"Debt-to-income ratio : {debt_to_income * 100:.1f}%   (bank allows up to 36%)")
print(f"Proposed loan payment: {payment_display:,.0f} Naira/month")
print(f"Total to repay       : {repayment_display:,.0f} Naira")
print(f"Total interest       : {interest_display:,.0f} Naira")
print(f"Interest is {interest_display / loan_amount * 100:.0f}% of what you borrow")
print()
print('-' * 60)
print()


if eligible:
    print("RESULT: ELIGIBLE ✅  - you meet the bank's rules of thumb.")
else:
    print("RESULT: NOT-ELIGIBLE ❌")
    print()
    if not dti_ok:
        print(" - Existing debts are too high relative to income.")
    if not payment_ok:
        print(" - The monthly payment would be too large for your income.")