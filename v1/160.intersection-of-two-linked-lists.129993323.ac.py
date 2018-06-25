#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (30.86%)
# Total Accepted:    177.5K
# Total Submissions: 575K
# Testcase Example:  'No intersection: []\n[]'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
# 
# For example, the following two linked lists: 
# 
# A:          a1 → a2
# ⁠                  ↘
# ⁠                    c1 → c2 → c3
# ⁠                  ↗            
# B:     b1 → b2 → b3
# 
# begin to intersect at node c1.
# 
# Notes:
# 
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns. 
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# 
# 
# 
# Credits:Special thanks to @stellari for adding this problem and creating all
# test cases.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
		#  4 star, 计算两个链表的长度差x，让让的链表先前进x步， 然后分别对比每个节点
        len_a, len_b = 0, 0
        node_a, node_b = headA, headB
        while node_a:
        	node_a = node_a.next
        	len_a += 1
        while node_b:
        	node_b = node_b.next
        	len_b += 1
        if len_b > len_a:
        	long = headB
        	short = headA
        else:
        	long = headA
        	short = headB
        gap = abs(len_a - len_b)
        while gap > 0:
        	long = long.next
        	gap -= 1
        while long and short:
        	if long.val == short.val and long.next is short.next:
        		return long
        	else:
        		long, short = long.next, short.next

# a = ListNode(3)
# b = ListNode(2)
# b.next = a

# s = Solution()
# print(s.getIntersectionNode(a, b).val)
