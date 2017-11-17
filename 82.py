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
    def deleteDuplicates(self, head):    # failed
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head.next
        new_head = ListNode(0)
        new_node = new_head
        pre = head.val
        while node:
            if node.next and node.next.val == node.val:
                node = node.next.next
            else:
                if node.val != pre:
                    new_node.next = ListNode(node.val)
                    new_node = new_node.next
                pre = node.val
                node = node.next
        return new_head.next
        
# if __name__ == "__main__":
#     n1 = ListNode(1)
#     n2 = ListNode(1)
#     n3 = ListNode(1)
#     n1.next = n2
#     n2.next = n3
#     r = Solution().deleteDuplicates(n1)
#     r.myprint()