
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 2 star, 直接替换val和next属性的值
        if not node:
            raise TypeError
        if not node.next:
            node = None
        node.val, node.next = node.next.val, node.next.next
