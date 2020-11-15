#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people = int(input("Between how many are you splitting the bill? "))
percentage = 1 + (percentage_tip / 100)
amount_to_pay_pp = (total_bill * percentage) / people
result_2decimals = round(amount_to_pay_pp, 2)
print(result_2decimals)
