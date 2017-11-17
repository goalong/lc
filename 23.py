# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):   # failed
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        node = head
        min_node = None
        while True:
        	min_node = lists[0]
        	for l in lists:
        		if not l:
        			continue
        		if l.val < min_node.val:
        			min_node = l
        	node.next = ListNode(min_node.val)
        	min_node = min_node.next
        return head.next

        