'''

In this task, you'll refactor a class that takes on multiple roles, making it more modular and easier to maintain.

The current LibraryManager class manages book details, borrower information, and notification tasks all in one place. Your job is to refactor the code to separate these concerns into distinct classes, each fulfilling a single responsibility, aiming to create a cleaner, more modular design.

'''

class LibraryManager :
# {
    def __init__(self, title, author, borrower_name, borrower_email) :
    # {
        self.title = title
        self.author = author
        self.borrower_name = borrower_name
        self.borrower_email = borrower_email
    # }
# }

class LibraryManagerSendDueDateReminder :
# {
    def send_due_date_reminder(self, borrower_email, author, title, due_date) :
    # {
        # print(f"Sending notification to {self.borrower_email}: "
              # f"'{self.title}' by {self.author} is due on {due_date}")
        print("Sending notification to", borrower_email, ':')
        print(title, "by", author, "is due on", due_date)
    # }
# }

def main() :
# {
    library_manager = LibraryManager("Fluent Python", "Luciano Ramalho", "John Doe", "john.doe@example.com")
    # library_manager.send_due_date_reminder("30th October 2023")
    library_manager_send_due_date_reminder = LibraryManagerSendDueDateReminder()
    library_manager_send_due_date_reminder.send_due_date_reminder(library_manager.borrower_email, library_manager.author, library_manager.title, "30th October 2023")
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

'''