# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):  # failed
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node.next:
        	if node.next.val == val:
        		node.next = node.next.next
        	node = node.next
        return dummy.next
        

# a = ListNode(6)
# b = ListNode(7)
# c = ListNode(9)
# b.next = c
# a.next = b

# Solution().removeElements(a, 7)
# while a:
# 	print(a.val)
# 	a = a.next