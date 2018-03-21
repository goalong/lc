





# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 3 star
        node = head  # 用node 表示目标链表的最后一个节点，从起始开始，如果有重复则只保留一个，忽略重复的，无重复则保留
        while node:
            if node.next:
                val = node.val
                if node.next.val != val:
                    node = node.next
                else:
                    while node.next and node.next.val == val:
                        node.next = node.next.next
            else:
                node = node.next
        return head