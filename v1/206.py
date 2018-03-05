# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head): # 
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
        	next = curr.next
        	curr.next = prev
        	prev = curr
        	curr = next
        return prev

# a = ListNode(8)
# b = ListNode(7)
# c = ListNode(5)

# b.next = c
# a.next = b

# n = Solution().reverseList(a)
# while n:
# 	print(n.val)
# 	n = n.next