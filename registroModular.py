from Fun_validations import validate_number, validate_text

students = []

def register_student():
        """Captures and validates student data (ID, Name, Age, Course, Status) and adds a new record to the list."""
        student_id = validate_number("Enter the student ID: ")
        name = validate_text("Enter the student name: ")
        age = validate_number("Enter student age: ")
        course = validate_text("Enter the student course: ")
        status_text = validate_text("Enter the status student (active/inactive): ")
            
        student={
                "Id": student_id,
                "Name":name,
                "Age":age,
                "Course": course,
                "Status": status_text
                }
        students.append(student)
        print("registered student")

def list_student():
    """Iterates through the global students list and displays all registered information in a formatted way."""
    print("LIST OF ENROLLED STUDENTS.")

    if len(students) == 0:
        print("No students registered.")
        return
    
    for student in students:
        print(f""" student
            Id={student["Id"]}
            Name={student["Name"]}
            Age={student["Age"]}
            Course={student["Course"]}
            Status={student["Status"]}
            """)


def search_student():
    """Prompts for a student ID and performs a search within the records to display the matching student's data."""
    search_id = validate_number("Enter ID student: ")

    found = False

    for student in students:
        if student["Id"] == search_id:
            print("Student found:")
            print(student)
            found = True
            break  
    
    if not found:                          
        print("Student not found.")


def update_student():
    """Locates a student by ID and allows the user to overwrite their Name, Age, Course, and Status with new validated data."""
    search_id = validate_number("Enter ID student: ")
    found = False  

    for student in students:
        if student["Id"] == search_id:
            found = True  
            print("Student found.")

            student["Name"] = validate_text("Enter new name student: ")
            student["Age"] = validate_number("Enter new age student: ")
            student["Course"] = validate_text("Enter new Course student: ")
            student["Status"] = input("Enter new status (active/inactive): ")
            
            print("Student updated successfully.")
            break
    
    if not found:  
        print("Student not found.")


def delete_student():
    """Searches for a student by ID and removes their record from the global list after a successful match."""
    search_id = validate_number("Enter ID to delete: ")
    found = False  

    for student in students:
        if student["Id"] == search_id:
            found = True  
            students.remove(student)
            print("Student deleted successfully.")
            break
            
    
    if not found: 
        print("Student not found.")


def show_menu():
    """Displays the main interface with all available administrative options for the Student Management System."""
    print("""
    STUDENT MANAGEMENT SYSTEM RIWI.

    (1) REGISTER STUDENT

    (2) LIST STUDENT

    (3) SEARCH STUDENT

    (4) UPDATE STUDENT

    (5) DELETE STUDENT

    (6) EXIT
    """)


option = ""

while option != "6":
    show_menu()
    option = input("Choose option: ")

    if option == "1":
        register_student()

    elif option == "2":
        list_student()

    elif option == "3":
        search_student()

    elif option == "4":
        update_student()

    elif option == "5":
        delete_student()

    elif option == "6":
        print("program finished")
    else:
        print("invalid option")