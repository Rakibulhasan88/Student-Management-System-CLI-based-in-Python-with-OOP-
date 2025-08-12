class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []
    
    def add_grade(self, subject, grade):
        self.grades[subject] = grade
    
    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        

    def display_student_info(self):
        super().display_person_info()
        print(f"Student ID: {self.student_id}, Grade: {self.grade}")

class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []  

    def add_student(self, student):
        if student.student_id not in self.students:
            self.students.append(student.student_id)
            student.enroll_course(self.course_name)

    def display_course_info(self):
        """Print course details and enrolled students."""
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print("Enrolled Students:")
        if self.students:
            for student in self.students:
                print(f"- {student.name} (ID: {student.student_id})")
        else:
            print("No students enrolled yet.")

students = {}
courses = {}
def add_new_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    address = input("Enter student's address: ")
    student_id = input("Enter student ID: ")
    if student_id in students:
        print("Student ID already exists. Please use a different ID.")
        return
    
    students[student_id] = Student(name, age, address, student_id)
    print(f"Student {name} (ID: {student_id}) added successfully.")

def add_new_course():
    course_name = input("Enter Course Name: ")
    course_code = input("Enter Course Code: ")
    instructor = input("Enter Instructor: ")

    if course_code in courses:
        print("Course code already exists.")
        return

    courses[course_code] = Course(course_name, course_code, instructor)
    print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

def enroll_student_in_course():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")

    if student_id not in students:
        print("Student not found.")
        return
    if course_code not in courses:
        print("Course not found.")
        return

    courses[course_code].add_student(students[student_id])
    print(f"Student {students[student_id].name} (ID: {student_id}) enrolled in {courses[course_code].course_name} (Code: {course_code}).")

def add_grade_for_student():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    grade = input("Enter Grade: ")

    if student_id not in students:
        print("Student not found.")
        return
    if course_code not in courses:
        print("Course not found.")
        return
    if course_code not in [code for code in courses if courses[code].course_name in students[student_id].courses]:
        print("Student is not enrolled in this course.")
        return

    students[student_id].add_grade(courses[course_code].course_name, grade)
    print(f"Grade {grade} added for {students[student_id].name} in {courses[course_code].course_name}.")
    
def display_student_details():
    student_id = input("Enter Student ID: ")
    if student_id not in students:
        print("Student not found.")
        return
    students[student_id].display_student_info()

def display_course_details():
    course_code = input("Enter Course Code: ")
    if course_code not in courses:
        print("Course not found.")
        return
    courses[course_code].display_course_info(students)


def main():
    while True:
        print("\n.....Student Management System.....")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")

        choice = input("Select Option: ")

        if choice == "1":
            add_new_student()
        elif choice == "2":
            add_new_course()
        elif choice == "3":
            enroll_student_in_course()
        elif choice == "4":
            add_grade_for_student()
        elif choice == "5":
            display_student_details()
        elif choice == "6":
            display_course_details()
        elif choice == "0":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
