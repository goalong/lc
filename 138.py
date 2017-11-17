# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):  # mark, smart solution
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node = head
        d = {}
        while node:
        	d[mode] = RandomListNode(node.label)
        	node = node.next
        node = head
        while node:
        	d[node].next = d[node.next]
        	d[node].random = d[node.random]
        	node = node.next
        return d[head]
