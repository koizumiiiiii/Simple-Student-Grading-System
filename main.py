from Student import Student

def main():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    
    student = Student(name, student_id)
    student.add_grades()
    student.display_info()
    
if __name__ == "__main__":
    main()