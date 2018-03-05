# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):  
        """
        :type head: ListNode
        :rtype: ListNode
        """
        left = ListNode(0)
        right = ListNode(0)
        right_head = right
        left_head = left
        index = 1
        p = head
        while p:
            next = p.next
            p.next = None
            if index % 2 == 0:
                right.next = p
                right = right.next
            else:
                left.next = p
                left = left.next
            p = next
            index += 1
        left.next = right_head.next
        return left_head.next

# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)

# a.next = b
# b.next = c
# c.next = d
# d.next = e


# s = Solution()
# head = s.oddEvenList(a)

# while head:
#     print(head.val)
#     head = head.next
