




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 3 star, 小心处理边界
        if not head:
            return head
        n = 0
        node = head
        while node:
            node = node.next
            n += 1
        k = k % n
        if k == 0:
            return head
        step = n - 1 - k
        p = head
        while step > 0:
            p = p.next
            step -= 1
        new_head = p.next
        last = p
        while p.next:
            p = p.next
        p.next = head
        last.next = None
        return new_head

# a, b, c, d = ListNode(1),
# ListNode(2), ListNode(3), ListNode(4)
# a.next, b.next, c.next, d.next = b, c, d, ListNode(5)

# while a:
#     print(a.val)
#     a = a.next
# a = ListNode(1)
# a = Solution().rotateRight(a, 1)
#
# while a:
#     print(a.val)
#     a = a.next