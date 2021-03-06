#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (33.40%)
# Total Accepted:    148K
# Total Submissions: 443K
# Testcase Example:  '[]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
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
        # 6 star, 把后半部分翻转，然后和前半部分逐一对照
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

