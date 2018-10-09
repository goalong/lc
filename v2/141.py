



class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 6 star, 判断链表有无环，使用双指针，一快一慢,如果有环，则快慢会相遇，否则即没有环
        # 快的一次走两步，慢的一次走一步
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
