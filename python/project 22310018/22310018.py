class Student:
    def __init__(self, name, student_id, stream):
        self.name = name
        self.student_id = student_id
        self.stream = stream
        self.grades = {}
        self.attendance = {'present': 0, 'absent': 0}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average(self):
        return sum(self.grades.values()) / len(self.grades)

    def get_highest_grade(self):
        return max(self.grades.values())

    def get_lowest_grade(self):
        return min(self.grades.values())

    def add_attendance(self, status):
        if status == 'present':
            self.attendance['present'] += 1
        elif status == 'absent':
            self.attendance['absent'] += 1

    def get_attendance(self):
        return self.attendance

    def check_passing_status(self):
        passing_grades = {
            "Arabic": {"scientific": 50, "literary": 75},
            "English": {"scientific": 50, "literary": 75},
            "Math": {"scientific": 100, "literary": 50},
            "Islamic Education": {"scientific": 50, "literary": 50},
            "Physics": {"scientific": 50, "literary": 0},
            "Chemistry": {"scientific": 50, "literary": 0},
            "Biology": {"scientific": 50, "literary": 0},
            "History": {"scientific": 0, "literary": 50},
            "Geography": {"scientific": 0, "literary": 50},
            "Scientific Culture": {"scientific": 0, "literary": 50},
            "Technology": {"scientific": 50, "literary": 50},
        }

        failed_subjects = []
        for subject, grade in self.grades.items():
            min_passing = passing_grades[subject][self.stream]
            if grade < min_passing:
                failed_subjects.append(subject)

        if failed_subjects:
            print(f"{self.name} has failed in the following subjects: {', '.join(failed_subjects)}")
        else:
            print(f"{self.name} has passed all subjects.")


class SchoolManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, student_id, stream):
        student = Student(name, student_id, stream)
        self.students.append(student)
        return student

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_student_grades(self, student_id):
        student = self.find_student(student_id)
        if student:
            print(f"Grades for {student.name} (ID: {student.student_id}):")
            for subject, grade in student.grades.items():
                print(f"{subject}: {grade}")
            print(f"Average: {student.calculate_average()}")
            print(f"Highest Grade: {student.get_highest_grade()}")
            print(f"Lowest Grade: {student.get_lowest_grade()}")
            student.check_passing_status()  # Check if the student passed all subjects
        else:
            print("Student not found.")

    def display_all_students_grades(self):
        for student in self.students:
            self.display_student_grades(student.student_id)
            print("-" * 30)

    def add_attendance(self, student_id, status):
        student = self.find_student(student_id)
        if student:
            student.add_attendance(status)
            print(f"Attendance recorded for {student.name}.")
        else:
            print("Student not found.")

    def print_student_certificate(self, student_id):
        student = self.find_student(student_id)
        if student:
            print("\n=== Student Certificate ===")
            print(f"Name: {student.name}")
            print(f"Student ID: {student.student_id}")
            print(f"Stream: {student.stream}")
            print("Grades:")
            for subject, grade in student.grades.items():
                print(f"{subject}: {grade}")
            print(f"Average: {student.calculate_average()}")
            print(f"Attendance: Present - {student.attendance['present']} days, Absent - {student.attendance['absent']} days")
            student.check_passing_status()  # Check if the student passed all subjects
            print("=" * 30)
        else:
            print("Student not found.")

    @staticmethod
    def sudoku_game():
        print("\n=== Sudoku Game ===")
        print("Enter your Sudoku solution (9x9 grid) row by row, using numbers 1-9 and 0 for empty cells:")
        grid = []
        for i in range(9):
            row = input(f"Row {i+1}: ").strip().split()
            row = [int(num) for num in row]
            grid.append(row)

        if SchoolManagementSystem.is_valid_sudoku(grid):
            print("Congratulations! Your Sudoku solution is correct.")
        else:
            print("Sorry, your Sudoku solution is incorrect.")

    @staticmethod
    def is_valid_sudoku(grid):
        # Check rows
        for i in range(9):
            row = [num for num in grid[i] if num != 0]
            if len(row) != len(set(row)):
                return False

        # Check columns
        for i in range(9):
            col = [grid[j][i] for j in range(9) if grid[j][i] != 0]
            if len(col) != len(set(col)):
                return False

        # Check 3x3 blocks
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3) if grid[x][y] != 0]
                if len(block) != len(set(block)):
                    return False

        return True


def main():
    school = SchoolManagementSystem()

    while True:
        print("\n=== Smart School Management System ===")
        print("1. Add Student and Grades")
        print("2. Display Grades of a Specific Student")
        print("3. Display Grades of All Students")
        print("4. Add Attendance")
        print("5. Print Student Certificate")
        print("6. Play Sudoku Game")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            stream = input("Enter student stream (scientific/literary): ")
            student = school.add_student(name, student_id, stream)

            # Add grades based on stream
            if stream == "scientific":
                subjects = ["Arabic", "English", "Math", "Islamic Education", "Physics", "Chemistry", "Biology", "Technology"]
            else:
                subjects = ["Arabic", "English", "Math", "Islamic Education", "History", "Geography", "Scientific Culture", "Technology"]

            for subject in subjects:
                while True:
                    try:
                        grade = float(input(f"Enter grade for {subject}: "))
                        if subject == "Arabic" and stream == "literary":
                            if 0 <= grade <= 150:
                                break
                            else:
                                print("Invalid grade! Arabic (Literary) must be between 0 and 150.")
                        elif subject == "English" and stream == "literary":
                            if 0 <= grade <= 150:
                                break
                            else:
                                print("Invalid grade! English (Literary) must be between 0 and 150.")
                        elif subject == "Math" and stream == "scientific":
                            if 0 <= grade <= 200:
                                break
                            else:
                                print("Invalid grade! Math (Scientific) must be between 0 and 200.")
                        elif 0 <= grade <= 100:
                            break
                        else:
                            print("Invalid grade! Grades must be between 0 and 100.")
                    except ValueError:
                        print("Invalid input! Please enter a number.")

                student.add_grade(subject, grade)

        elif choice == "2":
            student_id = input("Enter student ID: ")
            school.display_student_grades(student_id)

        elif choice == "3":
            school.display_all_students_grades()

        elif choice == "4":
            student_id = input("Enter student ID: ")
            status = input("Enter attendance status (present/absent): ")
            school.add_attendance(student_id, status)

        elif choice == "5":
            student_id = input("Enter student ID: ")
            school.print_student_certificate(student_id)

        elif choice == "6":
            SchoolManagementSystem.sudoku_game()

        elif choice == "7":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()