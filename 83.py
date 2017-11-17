# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)
        node = head
        new_node = new_head
        while node:
        	if node.next and node.next.val == node.val:
        		node = node.next
        	else:
        		new_node.next = ListNode(node.val)
        		node = node.next
        		new_node = new_node.next
        return new_head.next
        