#
# [147] Insertion Sort List
#
# https://leetcode.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (33.74%)
# Total Accepted:    115.9K
# Total Submissions: 343.6K
# Testcase Example:  '[]'
#
# Sort a linked list using insertion sort.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):  # smart, mark and pratice
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next


# a = ListNode(5)
# b = ListNode(3)
# c = ListNode(8)
# d = ListNode(7)
# e = ListNode(100)
# f = ListNode(7)

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

# head = a

# s = Solution()
# head = s.insertionSortList(a)

# while head:
#     print head
#     head = head.next



