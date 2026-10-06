student_name=input("Enter Name: ")
score_python=float(input("Python Score: "))
score_english=float(input("English Score: "))
score_maths=float(input("Mathematics Score: "))

print("\n")

average=(score_python+score_english+score_maths)/3

print("=========================")
print("   STUDENT RESULT  ")
print("=========================")
print(f"Studen: {student_name}")
print(f"Python:       {score_python}")
print(f"English:      {score_english}")
print(f"Mathematics:  {score_maths}")
print("--------------------")
print(f"Average: {average}")