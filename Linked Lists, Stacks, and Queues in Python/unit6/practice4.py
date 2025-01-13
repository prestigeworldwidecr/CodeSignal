'''

Great work, Voyager! You have mastered both the concepts and the practical applications of Linked Lists.

Now, let's deepen our understanding of the domain of Python Data Structures.

Consider an alien network. This network has a head node named "Zog". "Zog" would like to communicate with "Zak", located in the Alien Linked List network. Unfortunately, "Zak" doesn't yet exist in this network.

Could you write a portion of the Python script to add "Zak" to the network following "Zog" in this alien communication Linked List?

'''

# Python Script to Implement and Manipulate Linked List in Python

# Node class
class Node :
# {
    # Constructor to initialize the node object
    def __init__(self, data) :
    # {
        self.data = data  # Assign the data
        self.next = None  # Initialize the next node as null
    # }

# }

# LinkedList class
class LinkedList:
# {
    # Initialize the linked list with a head
    def __init__(self) :
    # {
        self.head = None
        self.tail = Node(None)
        self.size = 0
    # }
    
    # Function to add a node to the beginning of the linked list
    def push(self, new_data) :
    # {
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.tail = self.head
    # }

    # TODO: Add a method to insert a node after a specified node in the linked list.
    def insert(self, data) :
    # {
        
        if (self.head is None) :
        # {
            print('!')
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

    # Function to print the linked list
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

llist = LinkedList()

# Add nodes to the alien communication network
llist.push("Zog")
# TODO: Insert a new node "Zak" after "Zog" in the alien communication network.
llist.insert("Zak")
# Print the Alien Communication Network
llist.print_list() 

'''

***** BONEYARD *****

# print("head", self.head.data)
            # print('!', self, data)
        # print("head", self.head.data, "tail", self.tail.data)
        

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

'''