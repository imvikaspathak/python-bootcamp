#welcome to the tip calculator
#what was the total bill?
#what percentage tip would you like to give you 10,12,or15,
#how many people to split the bill
#each  should pay : $19:53

from typing import final


print("welcome to the tip calculator")
bill = float(input("what was total bill? $"))
tip = int(input("how much tip would you like to give? 10,12,or 15?"))
people =int(input("how many people to split the bill ?"))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/ people
final_amount = round (bill_per_person,2)
print(f"each person should pay ${final_amount}")
