'''

Welcome to the first practical exercise on constructors and object initialization! 🚀

In this task, we'll explore how to simplify object creation by improving constructor practices. The current code involves a constructor with complex logic, parsing data strings to initialize its attributes. Your task is to refactor this code by simplifying the constructor and providing clarity in object initialization.

'''

class Event :
# {
    def __init__(self, event_name, event_date, event_location, attendees_count) :
    # {
        self.event_name = event_name
        self.event_date = event_date
        self.event_location = event_location
        self.attendees_count = attendees_count
    # }

    @classmethod
    def from_string(cls, data_string) :
    # {
        data = data_string.split(',')
        return cls(data[0].strip(), data[1].strip(), data[2].strip(), int(data[3].strip()))
    # }

# }

def main() :
# {
    data_string = "Conference, 2023-12-25, New York,500"
    event_ = Event.from_string(data_string)
    # print(event_)
    print(event_.event_name)
    print(event_.event_date)
    print(event_.event_location)
    print(event_.attendees_count)
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

# data = data_string.split(',')

class Event :
# {
    def __init__(self, data_string) :
    # {
        data = data_string.split(',')
        self.name = data[0]
        self.date = data[1]
        self.location = data[2]
        self.attendees = int(data[3])
    # }

    def __str__(self) :
    # {
        return self.name + ',' + self.date + ',' + self.location + ',' + str(self.attendees)
    # }

# }

'''