'''

Welcome to the last lesson of the Clean Code with Multiple Classes course! Throughout this journey, we have delved into various aspects of clean coding, including class collaboration, dependency management, and the use of polymorphism. Today, we will focus on handling exceptions across classes in Python — a crucial skill for writing robust and clean Python code. Proper exception handling helps prevent the propagation of errors and enhances the reliability and maintainability of software.

Handling exceptions that span multiple classes can introduce several issues if not done correctly. Some of these include:

Loss of Exception Context: When exceptions are caught and re-raised without adequate information, it makes error diagnosis challenging.

Diminished Readability: When exception handling is complex and intertwined with business logic, it can obscure the main purpose of the code.

Referencing what we learned in the lesson on class collaboration and decoupling, maintaining loose coupling and high cohesion is equally important when dealing with exceptions.

To manage exceptions effectively across multiple classes, consider the following best practices:

Propagate Exceptions with Context: When re-raising exceptions, include context-specific information to facilitate debugging. Python allows for chaining exceptions using the raise ... from ... syntax for preserving the original exception context.

Use Python's Exception Hierarchy: Leverage Python's built-in exception classes and create custom exceptions to handle specific error scenarios, making your codebase cleaner and easier to maintain.

Keep Exception Handling Separate from Core Logic: Separate business logic from error handling to enhance readability and maintainability.

Proper exception handling provides clear error reporting without cluttering business logic.

Effective exception handling across class boundaries is crucial for maintaining clean and robust code. Here are some strategies and patterns that can help achieve this:

Custom Exception Classes

Creating custom exception classes allows you to encapsulate domain-specific error conditions with meaningful syntax and context, enhancing clarity and maintainability.

Example: Interacting with a Third-Party API

Consider a scenario where a service interacts with a third-party API:

Abstraction of Error Details: The DataAccessException in the example provides a high-level description of the error ("Failed to retrieve data from external service"), shielding the application from potentially sensitive or low-level details found in the ExternalServiceError. This abstraction benefits both security and readability.
Preservation of Context: The use of raise ... from ... ensures that the original ExternalServiceError is not entirely discarded. When raising a new exception using raise ... from ..., the previous exception (ExternalServiceError in this case) is preserved as the cause of the new exception (DataAccessException). This linkage is stored in the __cause__ attribute, allowing developers to trace back to the root cause during debugging, with an improved traceback that reveals the flow from the higher-level error back to the original one.
Improved Error Handling: This practice keeps the codebase clean and allows the application to respond to high-level errors consistently, without concern for the specific internal workings of the third-party API interaction.
Example: API Service with Custom Hierarchical Exceptions

This hierarchy demonstrates how more specific exceptions (like DataRetrievalException) can inherit from broader categories (APIServiceException) to handle domain-specific error conditions. The inclusion of a cause attribute allows for context preservation, promoting informative debugging without exposure.

Let's examine how exceptions propagate across classes using an example from an order processing application. Here's how exceptions are handled through different service layers:

The OrderService relies on the InventoryService to handle item reservations.
If the InventoryService encounters a problem and raises an InventoryException, such as when there are no items to reserve, the OrderService catches this exception.
The re-raising of a new OrderProcessingException with additional context relevant to order processing ensures that error handling is specific to the layer's purpose. This approach maintains distinct boundaries between application layers, ensuring context-specific error information is preserved across class boundaries without losing track of its origins.
These patterns and strategies help construct robust exception-handling mechanisms, enhancing the resilience and clarity of multi-class Python applications.

As we conclude this lesson on exception handling, remember the importance of designing your code to handle errors gracefully while maintaining the integrity and readability of your codebase. By using strategies like meaningful exception propagation, leveraging Python's exception hierarchy, and creating custom exception classes, you can elevate your Python programming skills.

Now, you're ready to tackle practice exercises that will reinforce these concepts. Apply what you've learned about exception handling in multi-class applications to write cleaner and more robust Python code!

'''

class DataAccessException(Exception) :
# {
    None
# }

def fetch_data() :
# {
    try :
    # {
        # Code to interact with the third-party API
        None
    # }

    except ExternalServiceError as e :
    # {
        raise DataAccessException("Failed to retrieve data from external service") from e
    # }

# }

class APIServiceException(Exception) :
# {
    """Base exception for API-related errors."""
    None
# }

class DataRetrievalException(APIServiceException) :
# {
    """Raised when data retrieval fails."""

    def __init__(self, message, cause=None) :
    # {
        super().__init__(message)
        self.cause = cause
    # }

# }

class InventoryException(Exception) :
# {
    None
# }

class OrderProcessingException(Exception) :
# {
    None
# }

class InventoryService :
# {
    def reserve_items(self, items) :
    # {
        if (items) :
        # {
            None
        # }

        else :
        # {
            raise InventoryException("No items in the order to reserve.")
        # }

    # }

# }

class OrderService :
# {
    def __init__(self, inventory_service) :
    # {
        self.inventory_service = inventory_service
    # }

    def process_order(self, order) :
    # {
        try :
        # {
            self.inventory_service.reserve_items(order.get_items())
        # }

        except InventoryException as e :
        # {
            raise OrderProcessingException("Failed to reserve items") from e
        # }

    # }

# }

'''

***** BONEYARD *****

'''