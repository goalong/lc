# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first, second = head, head
        for i in range(n-1):
        	first = first.next
        while first.next:
        	first, second = first.next, second.next
        second.next, second.val = second.next.next, second.next.val
        return head