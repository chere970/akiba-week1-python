name=input("Enter Your Name: ")
weight=float(input("Weight in kilo gram: "))
height=float(input("Height in meter: "))


bmi=weight/(height*height)

print("\n")
print("=============================")
print("        BMI REPORT    ")
print("=============================")

print(f"Name:     {name}")
print(f"Weight:   {weight}")
print(f"Height:   {height}")
print("\n")
print(f"BMI: {bmi}")

print("=============================")