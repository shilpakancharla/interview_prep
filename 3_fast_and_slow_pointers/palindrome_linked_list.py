"""
    Given the head of a singly linked list, return True if it is a palindrome.
"""

# Object used for ListNode initialization
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def is_palindrome(self, head):
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = slow
        slow = slow.next
        prev.next = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        fast = head
        slow = prev
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True