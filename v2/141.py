
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 5 star，快慢指针法， 一个一次走两步，一个一次走一步，
        # 当快的指针前进到为空或者其next为空时，说明是无环的，当快慢指针在行进中相等时说明是有环的
        slow = fast = head
        while slow:
            slow = slow.next
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            if slow == fast:
                return True
        return False
