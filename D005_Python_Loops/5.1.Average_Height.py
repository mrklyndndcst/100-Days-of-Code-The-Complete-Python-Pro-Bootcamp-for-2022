sum = 0
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# print(input("Input a list of student heights ").split())
# print(len(student_heights))
# print(n)
  sum += student_heights[n]
#  print(sum)
print(f"The average height of {n + 1} students are {round(sum/(n + 1))}cm")
#156 178 165 171 187