# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast.next:
        	fast = fast.next.next
        	slow = slow.next
        right = slow.next
        slow.next = None
        prev = None
        left = head
        while left:
        	next = left.next
        	left.next = prev
        	prev = left
        	left = next
        while prev and right:
        	if prev.val != right.val:
        		return False
        return True

a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(1)

a.next = b
b.next = c
c.next = d

s = Solution()
print s.isPalindrome(a)
