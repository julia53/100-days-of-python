import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


player_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scisors."))

rock_num = 0
paper_num = 1
scissors_num = 2


if player_choice == rock_num:
  print(rock)
elif player_choice == paper_num:
  print(paper)
else:
  print(scissors)

print("Computer Chose")
computer_choice = random.randint(0,2)

if computer_choice == rock_num:
  print(rock)
elif computer_choice == paper_num:
  print(paper)
else:
  print(scissors)


result_matrix = [
  ["Drew", "Lose", "Win"],
  ["Win", "Drew", "Lose"],
  ["Lose", "Win", "Drew"]
]

'''
if player_choice == computer_choice:
  print("Draw")
elif player_choice == scissors_num and computer_choice == paper_num:
  print("You Win")
elif player_choice == rock_num and computer_choice == scissors_num: 
  print("You Win")
elif player_choice == paper_num and computer_choice == rock_num:
  print("You Win")
elif player_choice == paper_num and computer_choice == scissors_num:
  print("Computer Wins")
elif player_choice == scissors_num and computer_choice == rock_num:
  print("Computer Wins")
elif player_choice == rock_num and computer_choice == paper_num:
  print("Computer Wins")
'''

print(f"You {result_matrix[player_choice][computer_choice]}")