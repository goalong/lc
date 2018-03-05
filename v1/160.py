# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a, len_b = 0, 0
        node_a, node_b = headA, headB
        while node_a:
        	node_a = node_a.next
        	len_a += 1
        while node_b:
        	node_b = node_b.next
        	len_b += 1
        if len_b > len_a:
        	long = headB
        	short = headA
        else:
        	long = headA
        	short = headB
        gap = abs(len_a - len_b)
        while gap > 0:
        	long = long.next
        	gap -= 1
        while long and short:
        	if long.val == short.val and long.next is short.next:
        		return long
        	else:
        		long, short = long.next, short.next

# a = ListNode(3)
# b = ListNode(2)
# b.next = a

# s = Solution()
# print(s.getIntersectionNode(a, b).val)