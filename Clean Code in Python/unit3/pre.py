'''

Welcome to your next step in mastering Clean Code! 🚀 Previously, we emphasized the significance of naming conventions in clean coding. Now, we delve into the realm of functions and methods, which serve as the backbone of application logic and are crucial for code organization and execution. Structuring these functions effectively is vital for enhancing the clarity and maintainability of a codebase. In this lesson, we'll explore best practices and techniques to ensure our code remains clean, efficient, and readable.

Clean Functions at a Glance
Let's outline the key principles for writing clean functions:

Keep functions small. Small functions are easier to read, comprehend, and maintain.
Focus on a single task. A function dedicated to one task is more reliable and simpler to debug.
Limit arguments to three or fewer. Excessive arguments complicate the function signature and make it difficult to understand and use.
Avoid boolean flags. Boolean flags can obscure the code's purpose; consider separate methods for different behaviors.
Eliminate side effects. Functions should avoid altering external states or depending on external changes to ensure predictability.
Implement the DRY principle. Employ helper functions to reuse code, minimizing redundancy and enhancing maintainability.
Now, let's take a closer look at each of these rules.

Functions should remain small, and if they become too large, consider splitting them into multiple, focused functions. While there's no fixed rule on what counts as large, a common guideline is around 15 to 25 lines of code, often defined by team conventions.

Below, you can see the process_order function, which is manageable but has the potential to become unwieldy over time:

Given that this process involves multiple steps, it can be improved by extracting each step into a dedicated function, as shown below:

In this code block, the process_order function orchestrates the whole order processing operation. It first validates the order and attempts payment processing. If either step fails, the function logs an error and returns early. Successful orders trigger the inventory update, customer notification, and finally, a success log entry.

In this code block, we define helper functions for each individual step in the order processing pipeline. validate_order checks the validity of the order, while process_payment handles the payment execution. Both functions log any failures. After these checks, update_inventory adjusts the stock levels, notify_customer communicates with the client, and log_order_processing captures a success message for completed orders.

A function should embody the principle of doing one thing only. If a function handles multiple responsibilities, it may include several logical sections. Below you can see the save_and_notify_user function, which is both too lengthy and does multiple different things at once:

To enhance this code, you can create two dedicated functions for saving the user and sending the welcome email. This results in dedicated responsibilities for each function and clearer coordination:

Here we define save_and_notify_user, which coordinates saving a user to the database and subsequently notifying them. It calls two separate functions to achieve these tasks, promoting clear separation of responsibilities.

In this code block, save_user handles database operations related to saving user data and manages any exceptions that arise. notify_user is responsible for sending notifications, using the send_welcome_email method, which contains the logic for email dispatch.

Try to keep the number of function arguments to a maximum of three, as having too many can make functions less understandable and harder to use effectively. 🤔

Consider the save_address function below with five arguments, which makes the function less clean:

A cleaner version encapsulates the details into an Address object, reducing the number of arguments and making the function signature clearer:

Boolean flags in functions can create confusion, as they often suggest multiple pathways or behaviors within a single function. Instead, use separate methods for distinct behaviors.

The set_flag function below uses a boolean flag to indicate user status, leading to potential complexity:

A side effect occurs when a function modifies some state outside its scope or relies on something external. This can lead to unpredictable behavior and reduce code reliability.

Below, the add_to_total function demonstrates a side effect by modifying an external state:

A cleaner version, calculate_total, performs the operation without altering any external state:

Avoid code repetition by introducing helper functions to reduce redundancy and improve maintainability.

The print_user_info and print_manager_info functions below repeat similar logic, violating the DRY principle:

To adhere to DRY principles, use a generalized print_info function that operates on a parent Person type:

In this lesson, we learned that clean functions are key to maintaining readable and maintainable code. By keeping functions small, adhering to the Single Responsibility Principle, limiting arguments, avoiding side effects, and embracing the DRY principle, you set a strong foundation for clean coding. Next, we'll practice these principles to further sharpen your coding skills!

'''

def process_order(order, inventory, logger) :
# {
    # Step 1: Validate the order
    if (order.is_valid()):
    # {
        None
    # }        
    
    else :
    # {
        logger.log("Invalid Order")
        return
    # }

    # Step 2: Process payment
    if (order.process_payment()) :
    # {
        None
    # }

    else :
    # {
        logger.log("Payment failed")
        return
    # }

    # Step 3: Update inventory
    inventory.update(order.get_items())

    # Step 4: Notify customer
    order.notify_customer()

    # Step 5: Log order processing
    logger.log("Order processed successfully")

# }

def process_order(order, inventory, logger) :
# {
    # Validate the order; if invalid, log and return
    if (validate_order(order, logger)) :
    # {
        None
    # }

    else :
    # {
        return
    # }

    # Process payment; if failed, log and return
    if (process_payment(order, logger)) :
    # {
        None
    # }

    else :
    # {
        return
    # }

    # Update the inventory based on the order
    update_inventory(order, inventory)
    # Notify the customer about the order
    notify_customer(order)
    # Log successful order processing
    log_order_processing(logger)

# }

def validate_order(order, logger) :
# {
    # Check if the order is valid, log if not
    if (order.is_valid()) :
    # {
        return True
    # }
    
    else :
    # {
        logger.log("Invalid Order")
        return False    
    # }

# }

def process_payment(order, logger) :
# {
    # Attempt to process payment, log failure
    if (order.process_payment()) :
    # {
        return True
    # }
    
    else :
    # {
        logger.log("Payment failed")
        return False
    # }

# }

def update_inventory(order, inventory) :
# {
    # Update inventory with items from order
    inventory.update(order.get_items())
# }

def notify_customer(order) :
# {
    # Notify the customer about order status
    order.notify_customer()
# }

def log_order_processing(logger) :
# {    
    # Log a successful order processing message
    logger.log("Order processed successfully")
# }

def save_and_notify_user(user, data_source) :
# {
    # Save user to the database
    sql = "INSERT INTO users (name, email) VALUES (?, ?)"

    try :
    # {
        connection = data_source.get_connection()
        statement = connection.prepare_statement(sql)
        # Set user details in the prepared statement
        statement.setString(1, user.get_name())
        statement.setString(2, user.get_email())

        # Execute the update query to save user
        statement.execute_update()
    # }

    except Exception as e :
    # {
        print("Exception:", e)  # Handle exception
    # }

    # Send a welcome email to the user
    send_welcome_email(user)

# }

def save_and_notify_user(user, data_source) :
# {
    # Save user to the database
    save_user(user, data_source)

    # Notify user with welcome email
    notify_user(user)
# }

def save_user(user, data_source) :
# {
    # SQL query to insert user data
    sql = "INSERT INTO users (name, email) VALUES (?, ?)"

    try :
    # {
        # Establish database connection and execute query
        connection = data_source.get_connection()
        statement = connection.prepare_statement(sql)
        statement.setString(1, user.get_name())
        statement.setString(2, user.get_email())
        statement.execute_update()
    # }

    except Exception as e:
    # {
        # Handle exception during database operation
        print(f"Exception: {e}")
    # }

# }

def notify_user(user) :
# {
    # Send a welcome email to the user
    send_welcome_email(user)
# }

def send_welcome_email(user) :
# {
    # Logic to send the welcome email
    print(f"Sending welcome email to {user.get_name()}...")
# }

def save_address(street, city, state, zip_code, country) :
# {
    # Logic to save address
    None
# }

def save_address(address) :
# {
    # Logic to save address
    None
# }

class Address :
# {
    def __init__(self, street, city, state, zip_code, country) :
    # {
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
    # }

# }

def set_flag(user, is_admin) :
# {
    # Logic based on flag
    None
# }

def grant_admin_privileges(user) :
# {
    # Logic for admin rights
    None
# }

def revoke_admin_privileges(user) :
# {
    # Logic to remove admin rights
    None
# }

# Not Clean - Side Effect
def add_to_total(value) :
# {
    global total
    total = total + value  # modifies external state
    return total
# }

# Clean - No Side Effect
def calculate_total(initial, value) :
# {
    return initial + value
# }

def print_user_info(user) :
# {
    print("Name:", user.name)
    print("Email:", user.email)
# }

def print_manager_info(manager) :
# {
    print("Name:", manager.name)
    print("Email:", manager.email)
# }

def print_info(person) :
# {
    print("Name:", person.name)
    print("Email:", person.email)
# }

'''

***** BONEYARD *****

'''