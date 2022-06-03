student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
student_grades = {}
criteria = {}

for n in range(0,71):
  criteria[n] = "Fail"
for n in range(71,81):
  criteria[n] = "Acceptable"
for n in range(81,91):
  criteria[n] = "Exceeds Expectations"
for n in range(91,101):
  criteria[n] = "Outstanding"
for score in student_scores:
  student_grades[score] = criteria[student_scores[score]]
# 🚨 Don't change the code below 👇
print(student_grades)
# 