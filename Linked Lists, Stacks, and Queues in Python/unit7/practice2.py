'''

Alright, Space Voyager! Now, let's solve a task that's as exciting as a hyperjump, and it's right within your grasp. The mission is to find if the number of elements in a singly linked list is even or odd - we're eyeing parity here, not the actual count. The linked list is provided as input, with the first element known as the head. Now, for output, return 'Even' if the linked list has an even number of elements and 'Odd' otherwise. Remember, edge cases might occur, like a list with no elements at all! So grab your space helmet and happy coding!

'''

class Node :
# {
    def __init__(self, data=None) :
    # {
        # implement this
        self.data = data
        self.next = None
    # }

# }

class LinkedList :
# {
    def __init__(self) :
    # {
        self.head = None
        self.tail = None # extra pointer to the last node
        self.data = None
        self.size = 0
    # }

    def add_node(self, data) :
    # {
        new_node = Node(data)

        if (self.head is None) : 
        # {
            self.head = new_node 
            self.tail = new_node # set tail point to the first node
        # }

        else :
        # {
            self.tail.next = new_node
            self.tail = new_node # update tail point to the new node
        # }

        self.size = self.size + 1

    # }

    def length_parity(self) :
    # {
        # implement this
        if (self.size % 2 == 1) :
        # {
            return "Odd"
        # }

        else :
        # {
            return "Even"
        # }

    # }

    def print_list(self) :
    # {
        current_node = self.head

        while(current_node) :
        # {
            print(current_node.data, end="->")
            current_node = current_node.next
        # }
    
    # }

# }

# Test cases:
linked_list = LinkedList()
linked_list.add_node(1) 
linked_list.add_node(2)
linked_list.add_node(3)
print(linked_list.length_parity()) # Expected 'Odd'
        
linked_list = LinkedList()
linked_list.add_node(10) 
linked_list.add_node(20)
linked_list.add_node(30)
linked_list.add_node(40)
print(linked_list.length_parity()) # Expected 'Even'
        
linked_list = LinkedList()
print(linked_list.length_parity()) # Expected 'Even'

'''

***** BONEYARD *****

# print('!')
# print(linked_list.print_list())
        # return self.size

'''