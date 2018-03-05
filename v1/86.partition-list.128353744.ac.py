#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (33.37%)
# Total Accepted:    118.8K
# Total Submissions: 356K
# Testcase Example:  '[]\n0'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# 
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_node = new_head
        node = head
        big = ListNode(0)
        big_node = big
        while node:
            if node.val < x:
                new_node.next = ListNode(node.val)
                new_node = new_node.next
            else:
                big_node.next = ListNode(node.val)
                big_node = big_node.next
            node = node.next
        new_node.next = big.next
        return new_head.next


        

# a = ListNode(2)
# b = ListNode(3)
# c = ListNode(1)

# a.next = b
# b.next = c

# s = Solution()

# head = s.partition(a, 2)
# while head:
#     print head
#     head = head.next
