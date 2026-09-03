**Day 3 — Loan Eligibility & Repayment Estimator**
Topic: Operators  arithmetic `(+ - * / // % **)`, comparison `(<= >= < >)`, and logical (and or not)

*What it does*
A mini bank `"credit officer"`. It takes your income, existing debts, and the loan
you want, then:

computes the real monthly repayment (the same amortization formula banks use),
checks the bank's two rules of thumb with comparison operators,
combines them with logical operators into one ELIGIBLE / NOT ELIGIBLE verdict.

📖 *How to use this folder (the learning method)*
Read the spec below.
Open:
`README.md` get full understanding of the program's requirments before opening the `main.py`
 
Run it: python3 main.py. Get it working.

*Concepts used (integrity check)*

Taught today (Day 3): arithmetic `(+ - * / // % **)`, comparison `(<=, >=, >)`,
logical (and, not), operator precedence (PEMDAS — brackets beat everything).
Previews (labelled):
if/else official topic: Day 9 (Conditionals). The verdict needs it to print
YES vs NO; the actual deciding is done by and/not (today's topic). It's marked
[PREVIEW] in the solution.
f-strings  official topic: Day 4 (Strings). Same handy preview as Day 2.


The spec
*The program should:*

Ask for 5 numbers: monthly income, existing monthly debt, loan amount,
annual interest rate (%), and loan term (years).
Compute with arithmetic operators:
months = years × 12
monthly interest rate = (rate / 100) / 12
growth = (1 + monthly rate) ^ months
monthly payment = loan × monthly rate × growth / (growth − 1)
total to repay = payment × months; total interest = total − loan
Check two rules with comparison operators:
debt-to-income ratio = existing debt / income, must be ≤ 0.36
payment must be ≤ 30% of income
Combine with logical operators (and / not) into one verdict.
Print a report, then the verdict.
These are illustrative rules of thumb for learning — not real bank policy.

Example run (your numbers will differ)
text

========================================================
LOAN ELIGIBILITY & REPAYMENT ESTIMATOR
========================================================
Your monthly income after tax (Naira): 500000
Existing monthly debt payments (Naira): 80000
Loan amount you want (Naira): 5000000
Annual interest rate in percent (e.g. 18): 18
Loan term in years (e.g. 5): 5
--------------------------------------------------------
Debt-to-income ratio : 16.0%   (bank allows up to 36%)
Proposed loan payment: 126,967 Naira/month
Total to repay       : 7,618,028 Naira
Total interest       : 2,618,028 Naira
Interest is 52% of RESULT: ELIGIBLE ✅  - you meet the bank's rules of thumb.what you borrow
--------------------------------------------------------

RESULT: ELIGIBLE ✅  - you meet the bank's rules of thumb.


*What I learned*

Operators are just symbols that do things to values: `*` multiplies, `**` raises to a power
`%` gives the remainder, `//` gives whole-number division reat for money and groups
Comparison operators produce `True` / `False`  the fuel for every decision
and `/` or `/` not combine `True` / `False` values into one answer
Brackets control operator precedence  the loan formula needs careful bracketing
Money: round only for display, keep full precision for the checks
Next

*Day 4  Strings → build a Password Generator & Strength Analyzer.*