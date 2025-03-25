'''

Hello and welcome to this lesson on comments and documentation in Python. In our previous lessons, we focused on the importance of meaningful naming and crafting well-organized functions to enhance the readability and maintainability of clean code. In this session, we'll shift our focus to mastering the art of writing effective comments and documentation, which act as guiding lights through complex sections of your code.

Commenting Practices at a Glance
Comments are a vital instrument for clarity, but they must be wielded judiciously. Below are scenarios where comments are truly beneficial:

Legal Comments: ✅ Use these to specify legal obligations and protect intellectual property.
Clarification: ✅ Aid understanding by explicating complex or non-obvious code logic.
Warning of Consequences: ✅ Highlight potentially risky operations to prevent unintended effects.
TODO Comments: ✅ Track tasks or improvements that need to be addressed in the future.
Documentation for Public APIs: ✅ Provide essential documentation using Python docstrings for API usability and developer guidance.
Here are situations where comments can be detrimental:

Redundant Comments: 🔴 Eliminate comments that merely reiterate code.
Noise Comments: 🔴 Avoid comments that offer no meaningful insight.
Commented-Out Code: 🔴 Remove old code unless retaining it is justified with a reason.
Unnecessary Documentation Comments: 🔴 Avoid excessive documentation for methods that don't require explanation, such as trivial ones.

Legal comments are key to ensuring proper acknowledgment and protection of intellectual property. They're used to specify licensing or copyright information, offering legal clarity to users and contributors about the code's usage terms. This practice not only fosters trust but also shields against potential legal disputes:

These comments ensure that users and contributors are aware of the legal rights and restrictions associated with the code.

Use comments to unravel complex logic in the code. It's not about stating the obvious but about offering insights where the code might be difficult to follow. This guidance can be invaluable for future developers or even your future self if you return to the code months or years later:

These comments serve as cautionary notes, alerting developers to potential impacts or risks within code execution. By highlighting operations that could lead to unintended side effects, they act as safeguards against misuse or oversight, especially in complex systems:

Mark sections with tasks or improvements that need attention. They're placeholders for future work, ensuring that ideas for enhancement or optimization don't get lost. Properly maintained TODO comments can help prioritize development focus and facilitate better project management:

In Python, docstrings are used to provide structured documentation essential for public API usability. They serve as detailed guides for developers looking to integrate or use the API, outlining how to interact with the code correctly and the expectations around inputs and outputs:

These comments help any developer understand how to properly use the function by describing parameters and return values.

Avoid comments that simply repeat what the code does. Redundant comments can clutter codebases, making code maintenance burdensome and distracting developers from meaningful insights. Strive to write code that is self-explanatory so that each comment adds genuine value:

Here, the comment is unnecessary as the code is self-explanatory.

Eliminate comments that don't add any meaningful insight. Noise comments serve no educational purpose and detract from the clarity of the code. Instead, they introduce more text for developers to parse, slowing down the comprehension process unnecessarily:

Noise comments obstruct the flow and make reading the code cumbersome.

Code that is commented out without explanation should be removed or clearly justified for being retained. Such remnants of old logic often confuse developers who may not easily discern the reasoning for its storage. Always annotate with context if retaining code sections temporarily:

Preserving commented-out code should only happen when necessary, with a reason provided.

Creating excessive inline comments for trivial functions adds clutter and should be avoided.

The example above demonstrates an unnecessary comment. Detailed inline comments for well-known functions like main() aren't typically needed.

In this lesson, we explored various types of comments and documentation in Python, emphasizing writing meaningful, succinct, and maintainable comments while avoiding redundant or noisy ones. You've also seen how to use Python docstrings effectively for documenting public APIs. As you proceed to the practice exercises, these guidelines will aid in honing your skills to create clean and well-documented Python code. Enjoy your practice and keep building those clean coding habits!

'''

# Copyright 2023, XYZ Corporation.
# Licensed under the Apache License, Version 2.0.

# Calculating square root using Newton's method for better precision
sqrt_value = compute_square_root(value)

# Warning: This operation will overwrite existing data
save_data_to_database(new_data)

# TODO: Add unit tests for edge cases
def process_input() :
# {
    # Implementation
    pass
# }

import math

def calculate_volume(radius, height) :
# {    
    
    """
    Returns the volume of a cylinder.

    :param radius: The radius of the cylinder's base.
    :param height: The height of the cylinder.
    :return: The calculated volume.
    """

    return math.pi * radius * radius * height

# }

count = len(items)  # Sets count to the size of items

# Now we increment i
i += 1
# End of increment

# old_value = compute_old_value(input)  # Unused due to new algorithm

def main() :
# {
    """The main function of the program."""
    pass
# }

'''

***** BONEYARD *****

'''