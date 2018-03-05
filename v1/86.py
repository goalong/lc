# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_node = new_head
        node = head
        big = ListNode(0)
        big_node = big
        while node:
            if node.val < x:
                new_node.next = ListNode(node.val)
                new_node = new_node.next
            else:
                big_node.next = ListNode(node.val)
                big_node = big_node.next
            node = node.next
        new_node.next = big.next
        return new_head.next


        

# a = ListNode(2)
# b = ListNode(3)
# c = ListNode(1)

# a.next = b
# b.next = c

# s = Solution()

# head = s.partition(a, 2)
# while head:
#     print head
#     head = head.next