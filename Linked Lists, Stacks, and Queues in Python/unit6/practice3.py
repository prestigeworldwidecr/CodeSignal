'''

Great work, Voyager! You've made it up to this point. The universe of data structures is vast, and we've only just begun to explore its surface.

Now, suppose you want to augment the LinkedList class with a size feature. Using your advanced Python skills, you've added a size property to the LinkedList class to track the number of nodes in the list. However, a bug appears to have emerged; the value of size doesn't seem to update correctly when a node is inserted or removed from the LinkedList.

The issue doesn't appear to be related to the syntax but seems to involve the program's logic and flow. Embrace your inner debugging superhero, identify the problem, and rectify it. Your task is to discover and fix this bug.

'''

class Node :
# {
    def __init__(self, data=None) :
    # {
        self.data = data
        self.next = None
    # }

# }

class LinkedList :
# {
    def __init__(self) :
    # {
        self.head = None
        self.tail = None
        self.size = 0
    # }

    def insert(self, data) :
    # {
        if (self.head is None) :
        # {
            self.head = Node(data)
            self.tail = self.head
        # }

        else :
        # {
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
        # }

        # self.size += 1
        self.size = self.size + 1

    # }

    def delete(self, data) :
    # {
        temp = self.head
        prev = Node(None)

        while (temp) :
        # {
            if (temp.data == data) :
            # {            
                self.head = temp.next
                temp = None
                self.size = self.size - 1
                return None

            # }

            else :
            # {
                None
            # }

            prev = temp
            temp = temp.next

        # }

        # self.size -= 1
        # self.size = self.size - 1

    # }

# }

list = LinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
print("Size of the linked list after insertions: ", list.size)  # Expected output: Size of the linked list after insertions: 3
list.delete(2)
print("Size of the linked list after deletion: ", list.size)  # Expected output: Size of the linked list after deletion: 2

'''

***** BONEYARD *****

else :
        # {
            temp = self.head

            while (temp.next):
            # {
                temp = temp.next
            # }

            temp.next = Node(data)
        # }

    temp = self.head

    if (temp is not None) :
    # {
        if (temp.value == value) :
        # {
            self.head = temp.next
            temp = None
            return None
        # }

        else :
        # {
            None
        # }
    
    # }

    else :
    # {
        None
    # }

if (prev) :
                # {
                    prev.next = temp.next
                # }

                else :
                # {
                    self.head = temp.next
                # }

                return None

'''