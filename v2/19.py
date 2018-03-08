




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 快慢指针法
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        step = 0
        while step < n:
            fast = fast.next
            step += 1
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        if slow.next:
            slow.next = slow.next.next
        return dummy.next

