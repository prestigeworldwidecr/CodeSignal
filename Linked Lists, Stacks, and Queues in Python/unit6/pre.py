'''

Welcome to our intriguing session for today! We're diving into an essential topic in computer science and data structures: Linked Lists. These structures comprise a sequence of nodes. Each node holds some data and a reference (a link) to the next node, thus forming a chain-like structure.

The concept of linked lists is leveraged in many real-world scenarios. For instance, in a music playlist where songs can be dynamically added, deleted, or reordered, linked lists serve as an excellent solution thanks to their efficient operations.

A linked list is a collection of nodes, each acting as a container for its data and a pointer (link) to the next node in the list. This link greatly facilitates sequential traversal through the list.

class Node 
{
    Data
    Pointer to Next Node
}

A node consists of two parts: Data, which contains the stored value (that could be any type such as number, string, etc.), and Pointer to Next Node, which holds the link to the next node in the sequence. When a node is initially created, next is set to None because there is no subsequent node to point to.

Think of it like a treasure hunt game, where each clue leads to the next one, and the chain continues until we reach the final destination.

Now you might wonder, why opt for linked lists when we already have arrays? The answer isn't definitive, as both have their uses. Choosing one over the other completely depends on the specific problem and requirements at hand.

Here are some points of comparison:

Memory Usage: Arrays allocate memory in a continuous block during their initialization. Advanced allocation may lead to unused memory if not all spaces are filled. On the other hand, linked lists allocate memory only when required, making efficient use of memory.

Insertion and Deletion: Inserting or deleting elements in an array is an expensive operation as it generally involves shifting elements to maintain element continuity. With linked lists, these operations are more efficient and take a constant time of 
O
(
1
)
O(1).

Access Time: Arrays provide constant time access to any element. Contrarily, linked lists require iteratively 
O
(
n
)
O(n) time for accessing an element. With arrays, you can directly jump to any index, while linked lists necessitate traversal from the start to the desired node.

While linked lists may not allow for constant time access like arrays do, they excel in insertion and deletion operations. Irrespective of the size of the list, insertion or deletion at any place takes constant time, i.e., 
O
(
1
)
O(1).

However, searching for a node in a linked list requires iterative traversal, and this can lead to the worst-case time complexity of 
O
(
n
)
O(n).

In order to understand and use linked lists effectively, we need to master certain operations such as insertion, deletion, and traversal. Let's break each one down:

Insertion: When we talk about insertion, we are referring to the process of adding a new node to the existing list.

Deletion: Contrarily, deletion describes the action of removing a specific node from the list.

Traversal: This operation is involved with accessing and scanning through the elements in the list, one by one.

For our discussion, let's use Python to create a small class-based implementation of a linked list. Following this structure, we can effectively understand and manipulate situated nodes in a linked list.

Let's discuss the methods of the LinkedList class in more detail.

When you call insert(value), a new node is created with the given value and added either as the head (if the list is empty) or as the next node of the current tail.

Calling delete(value) searches the list for a node with the given value. If the node is found, it is removed from the list, and the links are fixed to keep the list connected.

The delete() method begins by setting a temp reference to the head of the linked list. This temp reference will be used to traverse the list.

The first if statement checks if the head of the list is not None or, in other words, if the list is not empty. Then, inside the if block, it checks if the head node is the node to be deleted (i.e., its value matches the value parameter). If it is, the head is updated to be the next node in the list (potentially None if the head was the only node in the list), and then the old head node is deleted by setting temp to None.

If the head node is not the one to be deleted, the list is traversed in search of the node. The prev reference is updated as the current node before temp moves on to the next one. If at any point during the traversal, a node with a value matching the value parameter is found, the loop breaks, leaving temp pointing to the node to delete and prev pointing to its predecessor.

After traversal, if temp is None, this means the node to delete was not found, and the function returns. Otherwise, the predecessor's next reference (which currently points to the to-be-deleted node) is updated to point to the successor of the node to be deleted, thus excluding it from the list. The node is then deleted by setting temp to None.

The delete() method doesn't return any value. It either successfully deletes a node or quietly returns if the requested node is not found in the list.

When print() is called, it runs a while loop through each node in the list starting from the head. It prints the value of each node until it reaches a node where node.next is None.

'''

class Node :
# {
    def __init__(self, value) :
    # {
       self.value = value
       self.next = None
    # }

class LinkedList :
# {
    def __init__(self) :
    # {
       self.head = None
       self.tail = None
    # }

# }

def insert(self, value) :
# {
    if (self.head is None) :
    # {
        self.head = Node(value)
        self.tail = self.head
    # }

    else :
    # {
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
    # }

# }

# Defining the delete method
def delete(self, value) :
# {
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

# }

while (temp is not None) :
# {
    if (temp.value == value) :
    # {
        break
    # }

    else :
    # {
        None
    # }
        
    prev = temp
    temp = temp.next

# }

if (temp == None) :
# {
    return None
# }

else :
# {
    None
# }
    
prev.next = temp.next
temp = None

def print(self) :
# {
    temp = self.head
    
    while (temp is not None) :
    # {
        print(temp.value, end=" => ")
        temp = temp.next
    # }

# }

list = LinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
list.print() # Output: 1 => 2 => 3 =>
list.delete(2)
list.print() # Output: 1 => 3 =>

'''

***** BONEYARD *****

'''