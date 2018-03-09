#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (31.39%)
# Total Accepted:    119.8K
# Total Submissions: 381.6K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# You may not alter the values in the nodes, only nodes itself may be changed.
# 
# Only constant memory is allowed.
# 
# For example,
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # todo, 这个解法不符合要求, 需要看一下别的解法
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


        
