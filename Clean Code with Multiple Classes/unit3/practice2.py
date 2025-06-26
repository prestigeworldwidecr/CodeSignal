'''

Welcome to the second exercise on managing class dependencies! In this task, we're going to refactor a codebase that suffers from tight coupling issues between classes. Right now, a BookingService class has a direct dependency on a specific EmailNotification class, constraining its flexibility and making it harder to change or test. Your mission is to introduce an abstract base class NotificationService and allow the BookingService to operate with any implementation that inherits from this abstract base class. This will open up possibilities for different notification strategies in the future!

'''

from abc import ABC, abstractmethod

class NotificationService(ABC) :
# {
    @abstractmethod
    def notify(self, message: str) :
    # {
        None
    # }

# }

class EmailNotification(NotificationService) :
# {
    def notify(self, message: str) :
    # {
        print("Email sent:", message)
    # }

# }

class BookingService :
# {
    def __init__(self, email_notification) :
    # {
        self.email_notification = email_notification  # Dependency injection
    # }

    def process_booking(self, message: str) :
    # {
        self.email_notification.notify(message)
    # }

# }

def main() :
# {
    # print("Processing booking...")
    booking_service = BookingService(EmailNotification())
    booking_service.process_booking("Your booking is confirmed!")
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