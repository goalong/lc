



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
        # 首先遍历链表，创建一个各个节点对应的新的链表中的节点的映射，新的节点和原来对应节点的值label相同,
        # 接下来再次遍历链表，将新的节点的next和random属性给补上，这俩属性可以用前面的映射找到
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

