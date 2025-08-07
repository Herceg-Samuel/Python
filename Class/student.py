class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return "No students available"
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"

    
student1 = Student("Alex", 3.4)
student2 = Student("Mike", 4.0)
student3 = Student("John", 3.7)

print(Student.get_count())           # Total # of students: 3
print(Student.get_average_gpa())     # Average GPA: 3.70
