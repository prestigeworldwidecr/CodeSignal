'''

Welcome to the first practical exercise on applying the DRY principle! In this task, we'll focus on reducing code duplication by extracting methods. The current code contains a repetitive section that computes the average score of students in different classes. Your task is to refactor the code by introducing a separate method to handle this repeated logic, ensuring that the code remains clean and maintainable.

Nice effort! However, the practice specifically asks you to extract the average calculation into a separate function, not just use sum and len directly.

Want to give it another shot? Let me know if you need a hint!

'''

def compute_average(n) :
# {
    return sum(n) / len(n)
# }

def main() :
# {
    class_a_scores = [85.5, 90.0, 78.5, 88.0]
    class_b_scores = [92.0, 81.5, 79.0, 85.5]
    
    print("Average score for Class A:", compute_average(class_a_scores))
    print("Average score for Class B:", compute_average(class_b_scores))
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

for score in class_a_scores :
    # {
        total_a = total_a + score
    # }

    average_class_a = total_a / len(class_a_scores)

    total_b = 0

    for score in class_b_scores :
    # {
        total_b = total_b + score
    # }

    average_class_b = total_b / len(class_b_scores)

    
    # print(sum(class_a_scores))

    # total_a = 0

    

    

'''