"""
    Given 'head', the head of a linked list, determine if the linked list has a cycle
    in it. There is a cycle in a linked list if there is some node in the list that can be
    reached again by continuously the 'next' pointer. Internally, 'pos' is used to denote the
    index of the node that tail's next pointer is connected to. 

    Return true if these is a cycle in the linked list. Otherwise, return false.
"""
# Object used for ListNode initialization
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def has_cycle(self, head):
        fast = head
        slow = head 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
            if fast == slow:
                return True
        return False