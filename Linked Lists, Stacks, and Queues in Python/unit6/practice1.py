'''

Alright, Space Wanderer, time's a-wasting! Welcome to the practice session on implementing your very own Circular Linked List. Have you ever wondered about repeating cycles in music playlists, slideshow transitions, or a simple ticketing system?

What about creating a system that cycles through certain data values? Sounds fun, doesn't it? Well, that's exactly what a Circular Linked List accomplishes!

Your mission, should you choose to accept it, involves examining the code implementation of a circular linked list. Once you press the Run button, take note of the output and try to validate it against the expected output mentioned in the comments.

'''

# Python program to create a circular linked list

# Node class
class Node :
# {
    # Constructor to initialize the node
    def __init__(self, data) :
    # {
        self.data = data
        self.next = None
    # }
# }
  
# Class to form a Circular LinkedList with basic operations
class CircularLinkedList :
# {
    # Constructor to initialize the linked list
    def __init__(self) :
    # {
        self.head = None
    # }
    
    # Function to add new node to the end of Circular Linked List
    def append(self, data) :
    # {
        if (not self.head) :
        # {
            self.head = Node(data)
            self.head.next = self.head
        # }

        else :
        # {
            new_node = Node(data)
            cur = self.head

            while (cur.next != self.head) :
            # {
                cur = cur.next
            # }

            cur.next = new_node
            new_node.next = self.head
        # }

    # }
    
    # Function to display all nodes of Circular LinkedList
    def display(self) :
    # {
        flag = True
        nodes = []
        cur = self.head
        cycle_count = 0

        while (flag):
        # {
            nodes.append(cur.data)

            if (cur.next == self.head) :
            # {
                # cycle_count += 1
                cycle_count = cycle_count + 1

                if (cycle_count == 2) :
                # {
                    # break
                    flag = False
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

            cur = cur.next
        # }

        print(" -> ".join(map(str, nodes)))
    # }

# }
        
clist = CircularLinkedList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.display()  # Expected output: 1 -> 2 -> 3 -> 1 -> 2 -> 3

'''

***** BONEYARD *****

'''