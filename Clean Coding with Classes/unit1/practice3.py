'''

Welcome to the final task of this unit! Let's put everything we have learned about the Single Responsibility Principle (SRP) into practice. In this task, you'll refactor a class responsible for too many tasks into smaller, more focused classes, as a culmination of your learning in this unit.

The current SchoolSystem class handles student details, course enrollment, and notification sending. Your task is to refactor this code into separate classes, each fulfilling a single responsibility. This change will enhance the modularity and maintainability of the system.

Let's dive in and transform this complex class structure into a streamlined, well-organized system!

'''

class Student :
# {
    def __init__(self, student_name, student_email) :
    # {
        self.student_name = student_name
        self.student_email = student_email
    # }
# }

class Course :
# {
    def __init__(self, course_name) :
    # {
        self.course_name = course_name
    # }

    def enroll_course(self, student_name, course_name) :
    # {
        print(student_name, "enrolled in", course_name)
        # self.send_enrollment_confirmation(course)
    # }
# }

class School :
# {
    def send_enrollment_confirmation(self, student_email, course_name) :
    # {
        print("Sending enrollment confirmation to", student_email, "for the course:", course_name)
    # }
# }

def main() :
# {
    # school_system = SchoolSystem("Alice", "alice@example.com")
    # school_system.enroll_course("Python Programming")
    student_ = Student("Alice", "alice@example.com")
    course_ = Course("Python Programming")
    school_ = School()

    course_.enroll_course(student_.student_name, course_.course_name)
    school_.send_enrollment_confirmation(student_.student_name, course_.course_name)
# }

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


class SchoolSystem :
# {
    def __init__(self, student_name, student_email) :
    # {
        self.student_name = student_name
        self.student_email = student_email
    # }

# }

'''