employee_name=input("Employee Name: ")
basic_salary=float(input("Basic Salary: "))
transport_allowance=float(input("Transport Allowance: "))
food_allowance=float(input("Food Allowance: "))

gross_salary=basic_salary+transport_allowance+food_allowance

print("\n")
print("=============================")
print("  EMPLOYEE PAYSLIP  ")
print("=============================")
print(f"Employee: {employee_name} ETB")
print(f"Basic Salary: {basic_salary:.2f} ETb")
print(f"Transport Allowance: {transport_allowance:.2f} ETB")
print(f"Food Allowance {food_allowance} ETB")
print("--------------------------")
print(f"Gross Salary: {gross_salary} ETB")
print("============================")