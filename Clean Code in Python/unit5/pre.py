'''

Hey there! 🎉 You've reached the final part of the Clean Code Basics with Python course. Fantastic work! 🚀 We've covered vital concepts like naming conventions, function design, and clean coding practices to ensure your code remains maintainable and efficient. In this lesson, we'll concentrate on eliminating redundancies in your code. This means identifying and removing unnecessary clutter that can complicate maintenance. Let's plunge in and make your code as clean and efficient as possible! 🧹

A smaller, well-optimized codebase is your best friend, as long as it serves the business needs efficiently. Here’s what to watch for:

Unnecessary Comments: Comments that simply repeat what the code already indicates add unnecessary clutter.
Duplicate Code: Code snippets that appear in multiple locations with minimal changes are just extra baggage.
Lazy Classes: Classes that don't contribute meaningful functionality clutter your code's architecture.
Dead Code: Code that's no longer in use is like old furniture — merely occupying valuable space.
Speculative Generality: Code written for theoretical use cases that might never occur adds bloat.

You’ve heard it before: remove comments that the code itself explains. Here's a quick refresher:

The comment above repeats what the function name already clarifies. Keep your comments meaningful!

You've learned about the DRY principle — time to put it into practice! By extracting common logic into functions or methods, you simplify your code.



'''

# This function calculates the total
def calculate_total(a, b) :
# {
    return a + b
# }

def send_notification(user) :
# {
    # sending logic
    None
# }

def alert_user(user) :
# {
    # same sending logic
    None
# }

def notify_user(user) :
# {
    # sending logic
    None
# }

class DataWrapper :
# {
    def __init__(self, data) :
    # {
        self._data = data
    # }

    def get_data(self) :
    # {
        return self._data
    # }

    def set_data(self, value) :
    # {
        self._data = value
    # }

# }

def obsolete_function() :
# {
    # functionality no longer needed
    pass
# }

from typing import Union

def process_data(data: Union[str, int]) :
# {
    if isinstance(data, str) :
    # {
        # process logic for string
        pass
    # }

    else :
    # {
        # unnecessary generic handling that isn't required now
        pass
    # }
    
# }
'''

***** BONEYARD *****

'''