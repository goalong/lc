# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     def myPrint(self):
#         print(self.val)
#         if self.next:
#             self.next.myPrint()


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        extra = 0
        head = ListNode(0)
        node = head
        while l1 or l2:
            data1 = l1.val if l1 else 0
            data2 = l2.val if l2 else 0
            total = data2 + data1 + extra
            if total > 9:
                extra = 1
                total = total - 10
            else:
                extra = 0
            node.next = ListNode(total)
            node = node.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        if extra:
            node.next = ListNode(extra)
        return head.next



# if __name__ == "__main__":
#     list = ListNode(9)
#     list.next = ListNode(8)
#     print(Solution().addTwoNumbers(list, ListNode(1)).myPrint())