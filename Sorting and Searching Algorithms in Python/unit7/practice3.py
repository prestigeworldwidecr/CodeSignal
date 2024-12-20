'''

Alright, Stellar Navigator, it's time for some fun with tuples! Picture yourself handling enrollment at the Nova Corps Academy. You got a bunch of courses, each with a unique identifier - an integer and a name – a string. Now, like any good Space Ranger in training, we need to keep things organized. So, we'll sort these courses in descending order of the course ID.

You'll have a list of tuples, each containing two elements. The first one's an integer representing the unique course ID, and the second one's a string for the course name.

Remember that the course IDs are like fingerprints — no two are identical. But don't sweat it because there's always a course ID and a course name present.

And guess what? Your properly organized list should have the same tuples, just arranged in an order where higher course IDs are leading the way. Now, show them what you got!

'''

def sort_course_id(courses) :
# {
    # implement this
    return sorted(courses, key = lambda x: x[0], reverse = True)
# }

# test samples
test_courses = [(101, "Astrophysics"), (303, "Galactic Politics"), (202, "Quantum Mechanics"), (404, "Alien Communication")]

print(sort_course_id(test_courses)) # Expected: [(404, 'Alien Communication'), (303, 'Galactic Politics'), (202, 'Quantum Mechanics'), (101, 'Astrophysics')]

'''

*****BONEYARD*****

'''