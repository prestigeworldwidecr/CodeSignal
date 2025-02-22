"""

Exciting progress, code explorer! You"ve cracked Depth-First Search (DFS) and ventured deep into the maze of Graphs. Are you ready for more?

Using the DFS traversal, can you determine the prerequisites for a course? Let"s consider the academic courses as a graph where each node represents a course, and the edges illustrate the prerequisites. Certain parts of the code have already been provided. Your task is to navigate the rest of the course graph to fill in the missing details.

"""

# Define the graph using dictionary representation
university_courses = {
                        "Math": set(["Physics", "Computer Science"]),
                        "Physics": set(["Math", "Chemistry"]),
                        "Chemistry": set(["Physics"]),
                        "Computer Science": set(["Math"]),
                    }

def DFS(courses, start_course, passed_courses) :
# {
    """
    Function implementing the DFS algorithm to traverse the graph.
    """

    if (start_course in passed_courses) : # Check if the course was taken earlier
    # {
        return
    # }

    else :
    # {
        passed_courses.add(start_course) # Add the course to the set of passed courses
        print(start_course, end=" --> ")

        # TODO: Code the recursive call inside the DFS function
        for course in courses[start_course] :
        # {
            if (course in passed_courses) :
            # {
                None
            # }

            else :
            # {
                DFS(courses, course, passed_courses)
            # }

        # }
        
    # }

# }

passed_courses = set()
# Call the DFS function, start the traversal with "Math"
DFS(university_courses, "Math", passed_courses) 

"""

***** BONEYARD *****

"""