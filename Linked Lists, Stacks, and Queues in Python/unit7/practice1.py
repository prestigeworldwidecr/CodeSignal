'''

All right then, cosmic coder! We got a challenge straight from the stars! Suppose you have a singly linked list, and I want you to traverse it in reverse, say from tail to head. Interesting, yeah?

While you're racing through it like a comet, I want you to find a sum of every third element of the list.

Your input is the head of the linked list. Ah, and don't forget: the list might be empty. The output is the sum of every third element of the reversed list. Now, fire the thrusters and code away!

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

def find_sum(head) :
# {
    index = 1
    sum_ = 0
    tmp = 0
    stack = []

    while (head) :
    # {
        # implement this
        stack.append(head)
        head = head.next
    # }

    while (stack) :
    # {
        tmp = stack.pop().data
        
        # implement this
        if (index % 3 == 0) :
        # {
            sum_ = tmp + sum_
        # }

        else :
        # {
            None
        # }

        index = index + 1

    # }

    return sum_

# }

list = LinkedList()
list.insert(1)
list.insert(2)
list.insert(3)

print(list.print_list())
print(find_sum(list.head))

'''

***** BONEYARD *****

# print("Size of the linked list after insertions: ", list.size)  # Expected output: Size of the linked list after insertions: 3

# list.delete(2)
# print("Size of the linked list after deletion: ", list.size)  # Expected output: Size of the linked list after deletion: 2

print(stack)

# print("index", index, "index % 3", index % 3)
        
print("index", index, "index % 3", index % 3)

'''