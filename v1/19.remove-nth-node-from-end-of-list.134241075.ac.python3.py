#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (34.08%)
# Total Accepted:    231.5K
# Total Submissions: 679.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the nth node from the end of list and return its
# head.
# 
# For example,
# 
# 
# ⁠  Given linked list: 1->2->3->4->5, and n = 2.
# 
# ⁠  After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# Given n will always be valid.
# Try to do this in one pass.
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 4 star, 双指针
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy
        step = 0
        while step < n:
            first = first.next
            step += 1
        while first and first.next:
            first, second = first.next, second.next
        if second.next:
            second.next = second.next.next

        return dummy.next
