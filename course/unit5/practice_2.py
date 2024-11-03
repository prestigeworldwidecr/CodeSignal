'''

Congratulations on completing your first run, Space Voyager! Now, it's time for a deeper dive. Assume you are managing events within an event system.

Could you modify the starter code to update the description of the Python Webinar and verify the final event list? We need to clarify the Python Webinar is going to be focused on Data Structures, and we should also reschedule it to a different time.

Let's venture forth, astronaut!

'''

# Create a Python dictionary that acts as a hash table
event_system = {}

# Add upcoming events
event_system[1] = "Coding Bootcamp - Monday, 8:00 AM"
event_system[2] = "Python Webinar - Tuesday, 10:00 AM"
event_system[3] = "Data Science Meetup - Wednesday, 6:00 PM"

# TODO: Update the Python Webinar description
# Note: don't change previous definitions of `event_system` elements.

# Update upcoming events
# event_system[1] = "Coding Bootcamp - Thursday, 8:00 AM"
event_system[2] = "Python Webinar clearly stated it's focused on Data Structures - Tuesday, 01:00 PM"
# event_system[3] = "Data Science Meetup - Saturday, 6:00 PM"

# Print the updated events list
print("\nUpdated upcoming events:")

for event_id, event_desc in event_system.items() :
# {
    print(f"Event ID: {event_id}, Description: {event_desc}")
# }

'''

********
BONEYARD
********

It looks like you've updated all the events, but the task is to specifically update the "Python Webinar" to focus on "Data Structures" and change its time.

Which event ID corresponds to the "Python Webinar"?
How can you update just that event's description and time?
Give it a try! 😊

Good try, but that's not exactly right.

You need to update the "Python Webinar" to focus on "Data Structures" and change the time to "1:00 PM". Would you like some help with that? 🤔

'''