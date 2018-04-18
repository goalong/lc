#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (35.12%)
# Total Accepted:    235.7K
# Total Submissions: 671K
# Testcase Example:  '[]\nno cycle'
#
# 
# Given a linked list, determine if it has a cycle in it.
# 
# 
# 
# Follow up:
# Can you solve it without using extra space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 6 star, 快慢指针
        slow = fast = head
        while fast and fast.next:
        	fast = fast.next.next
        	slow = slow.next
        	if fast == slow:
        		return True
        return False
