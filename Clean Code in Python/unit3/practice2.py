'''

Hello! In this task, we will tackle the challenge of reducing the number of arguments in function signatures by refactoring the code. The current method responsible for calculating compensation uses too many arguments, which can be cumbersome and error-prone. Your goal is to create a helper class that groups these related parameters together, making the code more organized and self-explanatory. This approach enhances code clarity while maintaining functionality.

You'll be dealing with calculating employee compensation, including components like base salary, taxes, benefits, and overtime. Let’s make the method signature cleaner by utilizing a helper class!

'''

class CompensationDetails :
# {
    def __init__(self, base_salary, tax_rate, benefits, overtime_pay) :
    # {
        self.base_salary = base_salary
        self.tax_rate = tax_rate
        self.benefits = benefits
        self.overtime_pay = overtime_pay
    # }

    def calculate_compensation(self) :
    # {
        base_compensation = self.base_salary
        total_benefits = base_compensation + self.benefits
        subtotal_compensation = total_benefits + self.overtime_pay
        total_compensation = subtotal_compensation - (subtotal_compensation * self.tax_rate)
        
        return total_compensation
    # }

# }

# }

def main() :
# {
    base_salary = 5000.00
    tax_rate = 0.20
    benefits = 200.00
    overtime_pay = 300.00

    cd = CompensationDetails(base_salary, tax_rate, benefits, overtime_pay)

    # TODO: Refactor to use CompensationDetails class to encapsulate these parameters
    # total_compensation = calculate_compensation(base_salary, tax_rate, benefits, overtime_pay)
    print("Total Compensation:", cd.calculate_compensation())

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

def calculate_compensation(base_salary, tax_rate, benefits, overtime_pay) :
# {
    base_compensation = base_salary
    total_benefits = base_compensation + benefits
    subtotal_compensation = total_benefits + overtime_pay
    total_compensation = subtotal_compensation - (subtotal_compensation * tax_rate)
    
    return total_compensation
# }

'''