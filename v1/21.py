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


        