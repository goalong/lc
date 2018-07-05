
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 6 star, 双指针一快一慢，快的一次两步，慢的一次一步，在快指针到达终点时，
        # 慢指针到达中间位置，这里注意要对奇偶做处理，之后对慢指针及之后的后半段进行翻转，翻转之后与前半段逐一对比
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        prev = None
        cur = slow
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        left = head
        while prev and left:
            if left.val == prev.val:
                left = left.next
                prev = prev.next
            else:
                return False
        return True

a = ListNode(1)
a.next = ListNode(2)

print(Solution().isPalindrome(a))


