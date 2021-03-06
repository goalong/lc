


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 6 star, pass, 必须熟练掌握
        # 就是前一个节点，当前节点和下一个节点之间的变换关系
        node = head
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev