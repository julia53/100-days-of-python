#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters_s = random.sample(letters, nr_letters)
symbols_ = random.sample(numbers, nr_symbols)
numbers_s = random.sample(symbols, nr_numbers)
print("".join(letters_s + symbols_ + numbers_s))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = letters_s + symbols_ + numbers_s

result = ""
curr_password_len = len(password_list) - 1

while curr_password_len >= 0:
  random_index = random.randint(0, curr_password_len)
  random_letter = password_list[random_index]
  result = result + random_letter
  password_list.pop(random_index)
  curr_password_len = curr_password_len - 1

print(result)

