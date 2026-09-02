
# Day 2 — Job Offer Comparator

> **Topic:** Variables & Built-in Functions  
> **Goal:** Compare two job offers based on annual pay, monthly take-home, and commute time using core Python built-ins.

---

## 📌 Overview

Two job offers just landed on your table. This program stores both offers in variables, computes comparable numbers (monthly take-home, annual pay, commute time), and tells you which one is better using only built-in functions.

---

## 📖 How to Use This Folder (The Learning Method)

1. Read the specification below.
2. Open `main.py` and complete  **do not look at `solution.py` yet**.
3. Run the script:
   ```bash
   python3 main.py
Get it working successfully.

Open solution.py and compare approaches:

What did you do differently?

Which built-ins did you miss?

What did the solution do that you like?

📋 *The Specification*

The program should:

Ask for the same 5 details for Offer A and Offer B:

Job title

Company name

Annual salary (Naira)

Monthly allowance (Naira)

Daily commute in minutes

Store each detail in its own variable.

Convert the text from input() into numbers with float() / int().

Compute for both offers:

Monthly take-home: salary / 12 + allowance

Annual pay: salary + allowance * 12

Weekly commute: commute * 5

Yearly commute in hours: commute * 5 * 52 / 60

Print a comparison table using f-strings.

Pick the winner and print a verdict, using comparison operators (>, <, ==) and built-in functions where appropriate.

💻 **Example Run**
(Your numbers will differ depending on your inputs)


====================================================
                JOB OFFER COMPARATOR
====================================================
Offer A - Job title: Software Engineer
Offer A - Company: CompA
Offer A - Annual salary (Naira): 6000000
Offer A - Monthly allowance (Naira): 50000
Offer A - Daily commute (minutes): 60

Offer B - Job title: Backend Developer
Offer B - Company: CompB
Offer B - Annual salary (Naira): 7200000
Offer B - Monthly allowance (Naira): 30000
Offer B - Daily commute (minutes): 45
----------------------------------------------------
                      Offer A         Offer B
----------------------------------------------------
Role              Software Engr   Backend Developer
Company                 CompA             CompB
Monthly take-home        550,000          630,000
Annual pay            6,600,000        7,560,000
Commute / week              300              225 min
Commute / year              260              195 h
----------------------------------------------------


🧠 *Concepts Used*
Taught Today (Day 2):
Variables

input()

float() & int()

round()


Comparison operators (>, <, ==)

Previews (Labelled — you'll meet these officially later):
f-strings (f"Annual pay: {x:,.0f}") — Official topic: Day 4 (Strings). Too handy to wait. Want to stay 100% Day-2? Use print("Annual pay:", annual_pay_a) instead.

if/elif/else — Official topic: Day 9 (Conditionals). Only used for the final verdict, and marked [PREVIEW] in the solution.


💡 *What I Learned*

Variables store one value each; name them clearly (salary_a, not x).

input() always returns text — float()/int() convert it for math.

f-strings embed variables into strings — f"Hello {name}".

Comparison operators (>, <, ==) let programs make decisions.


⏭️ *Next Step*
Day 3 - Operators: *Build a Loan Eligibility & Repayment Estimator.*
