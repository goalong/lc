# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 3 star, 要求是不使用额外的空间，这个方法使用了一个集合记录所有已经访问的节点，如果重复访问到，说明就是环的起点
        # todo 不使用额外空间的方法
        memo = set()
        while head:
            if head in memo:
                return head
            memo.add(head)
            head = head.next
        return None
