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
    def rotateRight(self, head, k):  # failed
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        first, second = head, head
        for _ in range(k - 1):
            first = first.next
        while first.next:
            if first.next.next:
                first, second = first.next, second.next
            else:
                break
        new_head = second.next
        second.next = None
        new_node = new_head
        while new_node.next:
            new_node = new_node.next
        new_node.next = head
        return new_head


# if __name__ == "__main__":
#     l1 = ListNode(1)
#     l2 = ListNode(2)
#     l3 = ListNode(3)
#     l4 = ListNode(4)
#     l5 = ListNode(5)
#     l1.next = l2
#     l2.next = l3
#     l3.next = l4
#     l4.next = l5
#     result = Solution().rotateRight(l1, 2)
#     result.myprint()