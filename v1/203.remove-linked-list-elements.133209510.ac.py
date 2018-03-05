#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (33.27%)
# Total Accepted:    145.7K
# Total Submissions: 437.8K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6,  val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
# 
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 3 star.
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next
