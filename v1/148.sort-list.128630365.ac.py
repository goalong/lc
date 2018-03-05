#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (29.70%)
# Total Accepted:    127K
# Total Submissions: 427.7K
# Testcase Example:  '[]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
        	return head
        slow = fast = head
        while fast.next and fast.next.next:
        	fast = fast.next.next
        	slow = slow.next
        head1 = head
        head2 = slow.next
        slow.next = None
        left = self.sortList(head1)
        right = self.sortList(head2)
        return self.merge(left, right)


    def merge(self, left, right):
    	if left is None:
    		return right
    	if right is None:
    		return left
    	dummy = ListNode(0)
    	node = dummy
    	while left and right:
    		if left.val <= right.val:
    			node.next = left
    			left = left.next
    		else:
    			node.next = right
    			right = right.next
    		node = node.next
    	if left:
    		node.next = left
    	if right:
    		node.next = right
    	return dummy.next


    # def merge(self, head1, head2):
    #     if head1 == None: return head2
    #     if head2 == None: return head1
    #     dummy = ListNode(0)                             
    #     p = dummy
    #     while head1 and head2:
    #         if head1.val <= head2.val:
    #             p.next = head1
    #             head1 = head1.next
    #             p = p.next
    #         else:
    #             p.next = head2
    #             head2 = head2.next
    #             p = p.next
    #     if head1 == None:
    #         p.next = head2
    #     if head2 == None:
    #         p.next = head1
    #     return dummy.next
        
    # def sortList(self, head):
    #     if head == None or head.next == None:
    #         return head
    #     slow = head; fast = head                        
    #     while fast.next and fast.next.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     head1 = head
    #     head2 = slow.next
    #     slow.next = None                               
    #     head1 = self.sortList(head1)
    #     head2 = self.sortList(head2)
    #     head = self.merge(head1, head2)
    #     return head



# a = ListNode(3)
# b = ListNode(2)
# c = ListNode(1)

# a.next = b
# b.next = c

# s = Solution()
# head = s.sortList(a)

# while head:
#     print(head.val)
#     head = head.next




        
