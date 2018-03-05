#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (44.61%)
# Total Accepted:    88.3K
# Total Submissions: 197.9K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the
# value in the nodes.
# 
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
# 
# 
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.
# 
# 
# Note:
# The relative order inside both the even and odd groups should remain as it
# was in the input. 
# The first node is considered odd, the second node even and so on ...
# 
# 
# Credits:Special thanks to @DjangoUnchained for adding this problem and
# creating all test cases.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):  
        """
        :type head: ListNode
        :rtype: ListNode
        """
        left = ListNode(0)
        right = ListNode(0)
        right_head = right
        left_head = left
        index = 1
        p = head
        while p:
            next = p.next
            p.next = None
            if index % 2 == 0:
                right.next = p
                right = right.next
            else:
                left.next = p
                left = left.next
            p = next
            index += 1
        left.next = right_head.next
        return left_head.next

# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)

# a.next = b
# b.next = c
# c.next = d
# d.next = e


# s = Solution()
# head = s.oddEvenList(a)

# while head:
#     print(head.val)
#     head = head.next

