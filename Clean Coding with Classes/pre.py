'''

Welcome to the very first lesson of the "Clean Coding with Classes" course! In our previous journey through "Clean Code Basics" we focused on the foundational practices essential for writing maintainable and efficient software. Now, we transition to learning about crafting clean, well-organized classes. This lesson will highlight the importance of the Single Responsibility Principle (SRP), which serves as a vital guideline for creating classes that are straightforward, understandable, and easy to work with.

The Single Responsibility Principle (SRP) states that a class should have only one reason to change, meaning it should have only one job or responsibility. This principle contributes significantly to software design by ensuring each class has a single purpose. Adhering to the SRP results in cleaner, more modular, and more understandable code. The main benefits include enhanced readability, straightforward maintenance, and easier testing, making it a cornerstone of clean coding.

Let's explore what happens when a class doesn't follow the Single Responsibility Principle by examining a practical code snippet. Consider the following Report class:

Here, the Report class handles report generation, printing, saving, and emailing, which are distinct responsibilities. This violation of the SRP results in increased complexity; changes in one area may unintentionally affect others, making maintenance more challenging. For example, if you modify the generate_report method to improve the report format, it might require adjustments in the print_report, save_to_file, and send_by_email methods if they rely on specific format details. This interdependence elevates the risk of introducing bugs, as altering one responsibility can have cascading effects on others that seem unrelated but are affected by shared data or logic.

To better align with the Single Responsibility Principle, we need to refactor the Report class into multiple classes, each handling a single responsibility. Let's examine a refactored version:

In this refactoring, each class is responsible for only one task: Report generates the report, ReportPrinter handles printing, ReportSaver takes care of saving to a file, and EmailSender manages email sending. This division improves the modularity and testability of our code. Each class can now be understood, modified, and reused independently, reducing unintended side effects.

In this lesson, we explored the Single Responsibility Principle, a key aspect of clean coding that ensures each class has a single purpose. By adhering to the SRP, you create classes that are easier to maintain and test. We've seen how ill-structured classes can be refactored to improve modularity and code comprehension. Up next, you'll engage in practice exercises that will help reinforce your understanding of the SRP and elevate your coding skills.

'''

class Report :
# {
    def generate_report(self) :
    # {
        # Generate report logic
        return "Report"
    # }

    def print_report(self, report_content) :
    # {
        # Print report logic
        print(report_content)
    # }

    def save_to_file(self, report_content, file_path) :
    # {
        # Save report logic
        print("Saving report to", file_path, "...")
    # }

    def send_by_email(self, email, report_content) :
    # {
        # Send email logic
        print(f"Sending email to {email}")
    # }

# }

class Report :
# {
    def generate(self) :
    # {
        # Generate report logic
        return "Report"
    # }

# }

class ReportPrinter :
# {
    def print_report(self, report_content) :
    # {
        # Print report logic
        print(report_content)
    # }

# }

class ReportSaver :
# {
    def save_to_file(self, report_content, file_path) :
    # {
        # Save report logic
        print("Saving report to", file_path, "...")
    # }

# }

class EmailSender :
# {
    def send_by_email(self, email, report_content) :
    # {     
        # Send email logic
        print("Sending email to", email)
    # }

# }

'''

***** BONEYARD *****

'''