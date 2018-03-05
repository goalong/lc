#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (24.43%)
# Total Accepted:    131.8K
# Total Submissions: 539.7K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a list, rotate the list to the right by k places, where k is
# non-negative.
# 
# 
# 
# Example:
# 
# Given 1->2->3->4->5->NULL and k = 2,
# 
# return 4->5->1->2->3->NULL.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 4 star.
        if not head:
            return None
        cur = head
        n = 0
        last = None
        while cur:
            n += 1
            if cur.next is None:
                last = cur
            cur = cur.next
        k = k % n
        if k == 0:
            return head
        step = n - k - 1
        node = head
        while step > 0:
            node = node.next
            step -= 1
        new_head = node.next
        node.next = None
        last.next = head
        return new_head

