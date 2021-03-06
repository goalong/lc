#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (46.63%)
# Total Accepted:    322.2K
# Total Submissions: 691K
# Testcase Example:  '[]'
#
# Reverse a singly linked list.
# 
# click to show more hints.
# 
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
        	next = curr.next
        	curr.next = prev
        	prev = curr
        	curr = next
        return prev

a = ListNode(8)
b = ListNode(7)
c = ListNode(5)

b.next = c
a.next = b

n = Solution().reverseList(a)
while n:
	print(n.val)
	n = n.next
