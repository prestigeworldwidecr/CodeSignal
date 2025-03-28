'''

Welcome to the final task in this unit on comments and documentation! This time, we'll focus on understanding how to handle tone and brevity while documenting your code.

The code contains comments that are overly verbose and casual, sometimes cluttering the purpose they're trying to serve. Your goal is to refine these comments, make them succinct, and ensure they convey the intended meaning without unnecessary fluff.

The code is a hypothetical example of a "Student Management System," with some basic operations for handling student data. Bring clarity and professionalism to the comments!

Docstrings: Keep them brief and to the point. For example, instead of "This method here will do the addition of a student using both their name and a unique ID," you could say, "Adds a student with the given name and ID."

Inline Comments: Remove any casual language or unnecessary comments. For instance, "Yeah, it's basically going to add them to the database" can be simplified to "Add student to the database."

Code Structure: Ensure that the code structure is clean and follows Python conventions. Avoid using unnecessary braces or comments that don't add value.

'''

class StudentManager :
# {
    def __init__(self) :
    # {
        self.fullname = ""
        self.student_id = ""
    # }

    '''
    Adds a student with the given name and ID.
    '''
    def add_student(self, name, student_id) :
    # {
        """
        This method here will do the addition of a student using both their name and a unique ID.

        Args:
            name (str): The name of the student is what you'll put here.
            student_id (int): It's the identification number for the student.
        """
        # Add student to the database.
        print("Student", name, "with ID", student_id, "added!")
    # }

    def print_student_data(self) :
    # {
        print(self.fullname)
        print(self.student_id)

# }

def main() :
# {
    sm = StudentManager()
    sm.add_student("John Doe", 1001)
    sm.print_student_data()
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

***** BONEYARD*****


    def __init__(self, fullname, student_id) :
    # {
        self.fullname = fullname
        self.student_id = student_id
    # }

    # sm.add_student("John Doe", 1001)

def add_student(self, full_name, student_id) :
    # {
        """
        This method here will do the addition of a student using both their name and a unique ID.

        Args:
            name (str): The name of the student is what you'll put here.
            student_id (int): It's the identification number for the student.
        """

        # Yeah, it's basically going to add them to the database
        print("Student", name, "with ID", student_id, "added!")
    # }

'''