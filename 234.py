# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        right = slow
        prev = None
        left = head
        while right:
            next = right.next
            right.next = prev
            prev = right
            right = next
        while prev and left:
            if prev.val != left.val:
                return False
            prev, left = prev.next, left.next
        return True

# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(2)
# d = ListNode(1)

# a.next = b
# b.next = c
# c.next = d

# s = Solution()
# print s.isPalindrome(a)
