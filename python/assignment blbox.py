class Student:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0


class SchoolSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, id_number):
        student = Student(name, id_number)
        self.students.append(student)

    def calculate_bill(self, amount):
        tax_rate = 0.16
        tax = amount * tax_rate
        total_amount = amount + tax

        if amount > 150:
            daily_payment = total_amount / 20
            return total_amount, daily_payment
        else:
            return total_amount, None

    def display_students(self):
        for student in self.students:
            print(f"Student Name: {student.name}, ID Number: {student.id_number}, Average Grade: {student.get_average():.2f}")


# Example of usage
school_system = SchoolSystem()

# User input for adding students
num_students = int(input("Enter the number of students: "))
for _ in range(num_students):
    name = input("Enter student name: ")
    id_number = input("Enter student ID number: ")
    school_system.add_student(name, id_number)

# User input for adding grades
for student in school_system.students:
    num_grades = int(input(f"\nEnter the number of grades for {student.name}: "))
    for _ in range(num_grades):
        subject = input("Enter subject name: ")
        grade = float(input(f"Enter grade for {subject}: "))
        student.add_grade(subject, grade)

# User input for cafeteria bill
bill_amount = float(input("\nEnter the cafeteria bill amount: "))
total, daily_payment = school_system.calculate_bill(bill_amount)
print(f"\nTotal Amount: {total:.2f} Shekels")
if daily_payment:
    print(f"Daily Payment for Installment: {daily_payment:.2f} Shekels")

# Displaying student information
print("\nStudent Information:")
school_system.display_students()