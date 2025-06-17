'''

In this task, you'll work on identifying and fixing the "Inappropriate Intimacy" code smell. You'll encounter a scenario where a class has too much knowledge about and dependency on the internal details of another class. Your goal is to refactor the code to improve encapsulation and reduce the coupling between classes. This will involve modifying how classes interact with each other to achieve better separation of concerns.

'''

class Transcript :
# {
    def __init__(self, student) :
    # {
        self.student = student
        # self.a = 1
    # }

    def display_transcript(self) :
    # {
        print(self.student.full_transcript())
        #  = self._student
        # self.a = 2
    # }

# }

class Student :
# {
    def __init__(self, name, courses) :
    # {
        self.name = name
        self.courses = courses
    # }

    def full_transcript(self) :
    # {
        return "Student: " + self.name + ' ' + "Courses: " + ', '.join(self.courses)
    # }

# }

def main() :
# {
    transcript = Transcript(Student("John Doe", ["Math", "Physics", "Chemistry"])).display_transcript()
    # transcript.display_record()
# }

if (__name__ == "__main__") :
# {
    main()
# }

else:
# {
    None
# }

'''

***** BONEYARD *****

    def get_name(self) :
    # {
        return self.name
    # }

    def get_courses(self) :
    # {
        return self.courses
    # }

    def display_record(self) :
    # {
        print(f"Student: {self.student.get_name()}")
        print(f"Courses: {', '.join(self.student.get_courses())}")
    # }

'''