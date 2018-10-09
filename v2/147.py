


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 5 star, 对每个元素插入到适合的位置，前面是一个已排序的，后面每一个往前插入合适的位置
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next:
            # 下一个元素的值小于当前节点，需要往前移动到合适的位置
            if cur.next.val < cur.val:
                pre = dummy
                while pre.next.val < cur.next.val:
                    pre = pre.next
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next
                pre.next = temp
            else:
                cur = cur.next
        return dummy.next
