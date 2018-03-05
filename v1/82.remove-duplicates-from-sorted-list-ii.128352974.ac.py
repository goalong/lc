#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (29.90%)
# Total Accepted:    129.3K
# Total Submissions: 432.5K
# Testcase Example:  '[]'
#
# 
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# 
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#     def myprint(self):
#         print(self.val)
#         if self.next:
#             self.next.myprint()

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        is_repeat = False
        while curr.next:
            while curr.next.next and curr.next.val == curr.next.next.val:
                curr.next = curr.next.next
                is_repeat = True
            if is_repeat:
                curr.next = curr.next.next
                is_repeat = False
            else:
                curr = curr.next
        return dummy.next
        
# if __name__ == "__main__":
#     n1 = ListNode(1)
#     n2 = ListNode(1)
#     n3 = ListNode(1)
#     n1.next = n2
#     n2.next = n3
#     r = Solution().deleteDuplicates(n1)
#     r.myprint()
