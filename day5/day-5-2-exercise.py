# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

curr_max = 0

for curr_score in student_scores:
  if curr_score > curr_max:
    curr_max = curr_score
print(curr_max)
