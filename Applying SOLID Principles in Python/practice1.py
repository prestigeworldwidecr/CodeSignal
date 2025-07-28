'''

Welcome to the first task on SOLID principles! In this exercise, we’ll focus on the Single Responsibility Principle. The current code manages a university system where the Course class has multiple responsibilities, including managing course details and grading students. We need to refactor the code so that each class has a single responsibility, leading to more maintainable and understandable code.

Your task is to refactor the code to ensure that it adheres to the Single Responsibility Principle by distributing responsibilities across multiple classes. Let's dive in!

'''

class Student :
# {
    def __init__(self, student_name) :
    # {
        self.student_name = student_name
    # }

    def get_student_name(self) :
    # {
        return self.student_name
    # }

# }

class Grade :
# {
    def __init__(self) :
    # {
        self.grades = {}
    # }
    
    def assign_grade(self, student, grade) :
    # {    
        self.grades[student.get_student_name()] = grade
    # }

# }

class Course :
# {
    def __init__(self, name) :
        self.name = name
        self.students = []
        self.grades = {}
    # }

    def add_student(self, student) :
    # {
        self.students.append(student)
    # }    

    def add_grade(self, grades) :
    # {
        self.grades = grades
    # }

    def print_student_grades(self) :
    # {
        for student in self.students:
        # {
            print("Student:", student.get_student_name(), ", Grade: ", self.grades[student.get_student_name()])
        # }

    # }

# }
    
def main() :

    

    student1 = Student("John Doe")
    student2 = Student("Jane Smith")

    grade = Grade()
    grade.assign_grade(student1, 85.5)
    grade.assign_grade(student2, 92.0)

    course = Course("History 101")
    course.add_student(student1)
    course.add_student(student2)
    course.add_grade(grade.grades)

    print("Course:", course.name)
    course.print_student_grades()
    

if (__name__ == "__main__") :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****



# course.add_student(student1)
    # course.add_student(student2)
        

'''