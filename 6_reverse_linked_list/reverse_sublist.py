"""
    Reverse a linked list from position m to position n.
"""

# Linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Standard reverse function used to reverse a linked list
def reverse(head):
    prev = None
    curr = head

    while (curr): # Traversing the linked list
        next = curr.next # Setting the next node
        curr.next = prev # Set to None initially,
        prev = curr # Save data of previous node
        curr = next # Setting next current node
    
    return prev

# Reverse linked list from position m to n using reverse function
def reverse_between(head, m, n):
    if (m == n):
        return head
    
    # rev_start and rev_end is start and end of portion of linked list
    # that needs to be reversed
    # rev_prev is previous of starting position
    # rev_end_next is next of end of list to be reversed
    rev_start = None
    rev_prev = None
    rev_end = None
    rev_end_next = None

    # Find values of above pointers
    i = 1
    curr = head

    while (curr and i <= n):
        if (i < m):
            rev_prev = curr
        
        if (i == m):
            rev_start = curr

        if (i == n):
            rev_end = curr
            rev_end_next = curr.next
        
        curr = curr.next
        i += 1

    rev_end.next = None 

    # Reverse linked list starting with rev_start
    rev_end = revrse(rev_start)

    # If starting position was not head
    if (rev_prev):
        rev_prev.next = rev_end
    # If starting position was head
    else:
        head = rev_end

    rev_start.next = rev_end_next

    return head

# Function to add a new node at the beginning of the list
def push(head_ref, new_data):
    new_node = Node(new_data)
    new_node.data = new_data
    new_node.next = (head_ref)
    (head_ref) = new_node
    return head_ref

def prints(head):
    while (head != None):
        print(head.data, end = ' ')
        head = head.next
         
    print()