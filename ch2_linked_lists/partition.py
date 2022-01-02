"""
    Write code to partition a linked list around a value x, such that all nodes less than x
    come before all nodes greater than or equal to x. If x is contained within the list, the
    values of x only need to be after the elements less than x. The partition element x can
    appear anywhere in the "right partition", it does not need to appear between the left and
    right partition.
"""

"""
    Implement an algorithm to find the kth to last element of a singly linked list.
"""

# Object used for ListNode initialization
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while (temp): 
            print(temp.val)
            temp = temp.next

    # Function to push a node at the beginning
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node 
    
    # Delete the first occurrence 
    def delete_node(self, val):
        temp = self.head # Store head node
        
        # If the head node contains the value to be deleted
        if temp and temp.val == val:
            self.head = temp.next
            temp = None
            return

        # Search for key that needs to be deleted
        while (temp):
            if temp.val == val:
                break
            prev = temp
            temp = temp.next

        # If key was not present in linked list
        if not temp:
            return 

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

def partition(linked_list, val):
    temp = linked_list.head
    before = []
    after = []
    while (temp):
        if temp.val < val:
            before.append(temp.val)
        else:
            after.append(temp.val)
        temp = temp.next
    
    new_linked_list = LinkedList()
    new_linked_list.head = Node(before[0])
    new_temp = new_linked_list.head

    for i in range(1, len(before)):
        temp_node = Node(before[i])
        new_temp.next = temp_node
        new_temp = new_temp.next
    
    new_temp.next = Node(val)
    
    for item in after:
        temp_node = Node(item)
        new_temp.next = temp_node
        new_temp = new_temp.next

    return new_linked_list

# Driver code
linked_list = LinkedList()
linked_list.head = Node(3)
second = Node(5)
third = Node(8)
fourth = Node(5)
fifth = Node(10)
sixth = Node(2)
seventh = Node(1)
linked_list.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = seventh
new_linked_list = partition(linked_list, 5)
new_linked_list.print_list()