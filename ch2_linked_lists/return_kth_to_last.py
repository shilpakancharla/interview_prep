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

    def find_kth_to_last(self, k):
        if not self.head:
            return

        temp = self.head
        elements = []
        while (temp):
            elements.append(temp.val)
            temp = temp.next

        if k > len(elements):
            return
        
        return elements[-k]
    
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

# Driver code
linked_list = LinkedList()
linked_list.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(2)
fifth = Node(1)
linked_list.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
second_to_last = linked_list.find_kth_to_last(9) # Return second to last node
print(second_to_last)