#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (25.90%)
# Total Accepted:    147.6K
# Total Submissions: 569.7K
# Testcase Example:  '{}'
#
# 
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# 
# 
# Return a deep copy of the list.
# 
#
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        memo = {}
        node = head
        while node:
            memo[node] = RandomListNode(node.label)
            node = node.next
        memo[None] = None
        node = head
        while node:
            memo[node].next = memo[node.next]
            memo[node].random = memo[node.random]
            node = node.next
        return memo[head]
