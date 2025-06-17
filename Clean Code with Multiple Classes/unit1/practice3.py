'''

In this exercise, we’ll explore the "Middle Man" code smell. You’ll encounter a situation where a class serves no real purpose other than forwarding calls to another class. Your mission is to refactor the code to eliminate the middleman and optimize the structure of the classes. This will require modifying the main application class to directly use the responsible class for performing the actions.

'''

class Printer :
# {
    def __init__(self, content) :
    # {
        self.content = content
    # }
    
    def execute_print(self) :
    # {
        print("Printing:", self.content)
    # }

# }

def main() :
# {
    p = Printer("Hello, this is a test document!").execute_print()
    # print_manager.manage_print()
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

class PrintManager :
# {
    def __init__(self) :
    # {
        self.printer = Printer()
    # }

    def manage_print(self, content) :
    # {
        self.printer.execute_print(content)
    # }

# }

'''