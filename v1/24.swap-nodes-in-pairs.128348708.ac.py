#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (39.01%)
# Total Accepted:    204.5K
# Total Submissions: 524.2K
# Testcase Example:  '[]'
#
# 
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# 
# 
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
# 
# Your algorithm should use only constant space. You may not modify the values
# in the list, only nodes itself can be changed.
# 
#
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
