def main():
  grade = float(input("Enter Grade: "))
  numberGrade = is_valid_grade(grade)
  letterGrade = calc_letter_grade(numberGrade)
  print("Grade: " + letterGrade)
  return

def is_valid_grade(grade):
  while grade > 100 or grade < 0:
    grade = float(input("Please enter a grade between 0 and 100: "))
  return grade

def calc_letter_grade(grade):
  if grade >= 90:
    letter = "A"
  elif grade >= 80:
    letter = "B"
  elif grade >= 70:
    letter = "C"
  elif grade >= 60:
    letter = "D"
  else:
    letter = "F"
  return letter

main()