# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        index = 1
        node = head
        while node:
        	if index % 2 == 1:
        		if node.next:
        			node.val, node.next.val = node.next.val, node.val
        	node = node.next
        	index += 1
        return head