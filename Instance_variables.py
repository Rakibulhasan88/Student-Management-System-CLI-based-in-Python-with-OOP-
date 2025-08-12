class School:
    school_name="ABC High School" #class variable

    def __init__(self, name):
        self.student_name = name # instance variable

school1 = School("John Doe")
school2= School("Jane Smith")
print(f"School Name: {School.school_name}")
print(f"Student Name: {school1.student_name}")