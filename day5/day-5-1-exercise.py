# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total = 0
count = 0

#Write your code below this row 👇
for student in student_heights:
  total = total + student
  count = count + 1

print(f"The average height is {round(total/count)}")