class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grades(self):
        print("\nEnter grades for 3 subjects:")
        for i in range(1, 4):
            while True:
                try:
                    grade = float(input(f"Grade for subject {i}: "))
                    break
                except ValueError:
                    print("Please enter a valid number.")
            self.grades.append(grade)

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_grade_letter(self):
        avg = self.calculate_average()

        if avg >= 95:
            return '4.0'
        elif avg < 95 and avg >= 90:
            return '3.5'
        elif avg < 90 and avg >= 85:
            return '3.0'
        elif avg < 85 and avg >= 80:
            return '2.5'
        elif avg < 80 and avg >= 75:
            return '2.0'
        else:
            return 'Fail'

    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.calculate_average():.2f}")
        print(f"Grade Letter: {self.get_grade_letter()}")