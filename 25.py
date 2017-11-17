# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):  # failed
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = head

        data_list = []
        rs = []
        while node:
        	data_list.append(node.val)
        	node = node.next
        	if len(data_list) == k:
        		rs.extend(data_list[::-1])
        		data_list = []
        if data_list:
        	rs.extend(data_list)
        new_head = ListNode(0)
        new_node = new_head
        for i in rs:
        	new_node.next = ListNode(i)
        	new_node = new_node.next
        return new_head.next


        