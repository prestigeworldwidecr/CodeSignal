'''

Well done, Space Voyager! We're on the home stretch; this is the last practice exercise for hash tables. You've aced all the tasks thus far, but can you handle this one on your own?

In our HR system, we maintain an employee database. Each employee is assigned a unique ID, and their role is tracked against this ID in a Python dictionary, which constitutes our hash table. Your task is to create an initial database with various roles, then simulate a scenario involving a promotion and an employee departure while updating the database accordingly.

Remember, this requires the addition, retrieval, and deletion operations that we've learned about in addition to the time complexity analysis for these operations. Good luck!

'''

# TODO: Create a Python dictionary to serve as a hash table
employee_database = {}

# TODO: Add employee names with their roles to the dictionary
employee_database["Rebeca Flores"] = "Administrative Assistant"
employee_database["Ana Hemkes"] = "Waitress"
employee_database["Marie Maier"] = "Bartender"

# TODO: Print the initial employee database
print("Initial Employee Database:")
print("--------------------------")

for employee_name, employee_role in employee_database.items():
# {
    print("Employee Name: ", employee_name, "\tEmployee Role: ", employee_role)
# }

print()

# TODO: Update the role of an employee in the database
employee_database["Ana Hemkes"] = "Dishwasher"

# TODO: Print the database after the employee role update
print("Updated Employee Database:")
print("--------------------------")

for employee_name, employee_role in employee_database.items():
# {
    print("Employee Name: ", employee_name, "\tEmployee Role: ", employee_role)
# }

print()

# TODO: Remove an employee from the database
del employee_database["Ana Hemkes"]

# TODO: Print the final employee database after the removal
print("Final Employee Database:")
print("--------------------------")

for employee_name, employee_role in employee_database.items():
# {
    print("Employee Name: ", employee_name, "\tEmployee Role: ", employee_role)
# }

'''

********
BONEYARD
********

Well done, Space Voyager! We're on the home stretch; this is the last practice exercise for hash tables. You've aced all the tasks thus far, but can you handle this one on your own?

In our HR system, we maintain an employee database. Each employee is assigned a unique ID, and their role is tracked against this ID in a Python dictionary, which constitutes our hash table. Your task is to create an initial database with various roles, then simulate a scenario involving a promotion and an employee departure while updating the database accordingly.

Remember, this requires the addition, retrieval, and deletion operations that we've learned about in addition to the time complexity analysis for these operations. Good luck!

'''