# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_until_90 = 90 - int(age)
months_until_90 = years_until_90 * 12
weeks_until_90 = years_until_90 * 52
days_until_90 = years_until_90 * 365

print(f"You have {days_until_90} days, {months_until_90} months, {weeks_until_90} weeks left")