#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (31.27%)
# Total Accepted:    133.3K
# Total Submissions: 426.3K
# Testcase Example:  '[5]\n1\n1'
#
# 
# Reverse a linked list from position m to n. Do it in-place and in
# one-pass.
# 
# 
# 
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# 
# 
# return 1->4->3->2->5->NULL.
# 
# 
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.
# 
#
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        index = 1
        node = head
        prev = dummy
        left, right = None, None
        before_left = None
        after_right = None
        if m != n:

            while node:
                if index < m:
                    prev = node
                    node = node.next
                    index += 1
                elif n >= index >= m:
                    next = node.next
                    if index == m:
                        left = node
                        before_left = prev
                    elif index == n:
                        right = node

                    node.next = prev
                    prev = node
                    node = next
                    index += 1
                else:
                    after_right = node
                    break
            before_left.next = right
            left.next = after_right
        return dummy.next
