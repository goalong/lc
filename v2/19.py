




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
        # 4 star, 双指针法, 使用了哑节点，将其指向链表的头节点，
        # 第一个指针从哑节点开始往前前进n步，然后第二个节点和第一个节点一同往前遍历，
        # 直到第一个指针到达链表末尾，这时第二个指针指向的就是目标节点
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

