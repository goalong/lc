#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (40.19%)
# Total Accepted:    225K
# Total Submissions: 559.7K
# Testcase Example:  '[]'
#
# 
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# 
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 3 star.
        dummy = ListNode(0)
        dummy.next = head
        current = head
        while current:
            if current.next and current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next

