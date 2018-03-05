#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (40.64%)
# Total Accepted:    318.6K
# Total Submissions: 784.1K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        node = head
        while l1 and l2:
        	if l1.val <= l2.val:
        		node.next = ListNode(l1.val)
        		l1 = l1.next
        	else:
        		node.next = ListNode(l2.val)
        		l2 = l2.next
        	node = node.next
        if l1:
        	node.next = l1
        if l2:
        	node.next = l2
        return head.next

# if __name__ == "__main__":
#     assert Solution().mergeTwoLists(ListNode(1), ListNode(2)).val == 1


        
