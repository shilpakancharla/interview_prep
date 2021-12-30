"""
    Reverse a linked list in a group of a given size k.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverse(self, head, k):
        if head == None:
            return None
        current = head 
        next = None
        prev = None
        count = 0

        # Reverse first k nodes of the linked list
        while (current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current 
            current = next
            count += 1

        # next is now a pointer to the (k + 1)th node
        # Recursively call for the list starting from current
        # Make rest of the list as next of first node
        if next is not None:
            head.next = self.reverse(next, k)

        return prev # prev is new head of input list

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next