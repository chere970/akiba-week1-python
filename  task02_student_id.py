def create_id_card():

    print("   ENTER STUDENT INFORMATION ")
    student_name=input("Enter you name: ")
    student_id=input("Your ID: ")
    department=input("Department: ")
    year=input("Academic Year: ")
    university=input("Unversity: ")
    phone_number=input("Phone number: ")

    card_width=48
    content_width=card_width-2

    title="AKIBA STUDNET CARD".center(content_width)
    name_field=f"Name: {student_name}".ljust(content_width)
    id_field=f"ID: {student_id}".ljust(content_width)
    department_field=f"Department: {department}".ljust(content_width)
    year_field=f"Year: {year}".ljust(content_width)
    university_field=f"University: {university}".ljust(content_width)
    phone_field=f"Phone {phone_number}".ljust(content_width)

    print("+" + "-" * content_width + "+")
    print(f"| {title}  |")
    print("+" + "-" * content_width + "+")
    print(f"|  {name_field} |")
    print(f"|  {id_field}  |")
    print(f"|  {department_field}  |")
    print(f"|  {year_field}  |")
    print(f"|  {university_field}  |" )
    print(f"|  {phone_field}  |" ) 
    print("+" + "-" * content_width + "+")

if __name__=="__main_":
     create_id_card()