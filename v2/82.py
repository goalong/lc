





# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 6 star, 需多练习
        # 思路类似双指针
        if not head:
            return None
        dummy = ListNode(-0xffffffff)
        dummy.next = head
        node = head
        _node = dummy # _node变量用来记录想要的目标链表的最后一个节点，从dummy节点开始，对后边的节点，如果节点重复则略过，不重复则往链表上接
        while node:
            if node.next:
                if node.val != node.next.val:
                    _node.next = node
                    node = node.next
                    _node = _node.next
                else:
                    val = node.val
                    while node and node.val == val:
                        node = node.next
            else:
                _node.next = node
                node = node.next
                _node = _node.next
        _node.next = None
        return dummy.next


# a = ListNode(1)
# a.next = ListNode(2)
# a.next.next = ListNode(2)
# Solution().deleteDuplicates(a)