print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
#converting the input to int as input is seen as string
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

#Adding Calculations to the input
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
#dividing the total bill to the number of people
bill_per_person = total_bill / people
#rounding it to 2 decimals
final_amount = round(bill_per_person, 2)
