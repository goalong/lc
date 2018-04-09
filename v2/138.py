



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
        # 6 star，必须掌握，未理解
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

