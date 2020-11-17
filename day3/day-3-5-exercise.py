# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = (name1 + name2).lower()
true_score = names.count("t") + names.count("r") + names.count("u") + names.count("e")
love_score = names.count("l") + names.count("o") + names.count("v") + names.count("e")
total_score = (true_score * 10) + (love_score)

if (total_score <= 10) or (total_score >= 90):
  print(f"Your score is {total_score}. You go together like coke and mentos.")
if (total_score >=40) and (total_score <= 50):
  print(f"Your score is {total_score}. You are alright together")
else:
  print(f"Your score is {total_score}.")
