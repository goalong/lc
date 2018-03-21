





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # 4 star, 用一个新的链表存储大于等于x的节点, 多练习，写了几次才bug free
        big_head = ListNode(0)
        small_head = ListNode(0)
        small_head.next = head
        node = head
        _node = big_head
        prev = small_head
        while node:
            if node.val < x:
                prev = node
                node = node.next
            else:
                _node.next = ListNode(node.val)
                _node = _node.next
                prev.next = node.next
                node = node.next
        prev.next = big_head.next
        return small_head.next

# a = ListNode(1)
# a.next = ListNode(1)
# Solution().partition(a, 0)