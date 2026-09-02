
role_a = input("Offer A - Job title: ")
company_a = input("Offer A - Company: ")
salary_a = float(input("Offer A - Annual salary (Naira): "))
allowance_a = float(input("Offer A - Monthly allowance (Naira): "))
commute_a = int(input("Offer A - Daily commute (minutes): "))



role_b = input("Offer B - Job title: ")
company_b = input("Offer B - Company: ")
salary_b = float(input("Offer B - Annual salary (Naira): "))
allowance_b = float(input("Offer B - Monthly allowance (Naira): "))
commute_b = int(input("Offer B - Daily commute (minutes): "))


monthly_take_home_a = round(salary_a / 12 + allowance_a, 2)
monthly_take_home_b = round(salary_b / 12 + allowance_b, 2)


annual_pay_a      = round(salary_a + (allowance_a * 12),2)
annual_pay_b       = round(salary_b + (allowance_b * 12),2)


weekly_commute_a    = commute_a * 5  
weekly_commute_b    = commute_b * 5  


commute_hours_yr_a  = round(commute_a * 5 * 52 / 60, 2)
commute_hours_yr_b  = round(commute_b * 5 * 52 / 60 , 2)





print()
print("-" * 62)
print(f"{'':<22} {'Offer A':>18} {'Offer B':>18}")
print("-" * 62)
print(f"{'Role':<22} {role_a:>18} {role_b:>18}")
print(f"{'Company':<22} {company_a:>18} {company_b:>18}")
print(f"{'Monthly take-home':<22} {monthly_take_home_a:>15,.0f} {monthly_take_home_b:>15,.0f}")
print(f"{'Annual pay':<22} {annual_pay_a:>15,.0f} {annual_pay_b:>15,.0f}")
print(f"{'Commute / week':<22} {weekly_commute_a:>18} {weekly_commute_b:>18} min")
print(f"{'Commute / year':<22} {commute_hours_yr_a:>18} {commute_hours_yr_b:>18} h")
print("-" * 60)

if annual_pay_a > annual_pay_b:  
      print(f"{company_a} pays more!")
elif annual_pay_b > annual_pay_a:
       print(f"{company_b} pays more!")
else:
       print(f"It's a tie! just follow your guts")
print()