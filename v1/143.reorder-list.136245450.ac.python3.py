#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (26.62%)
# Total Accepted:    108.5K
# Total Submissions: 407.7K
# Testcase Example:  '[1,2,3,4]'
#
# 
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# 
# You must do this in-place without altering the nodes' values.
# 
# 
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:                                                                    
    def reorderList(self, head):                                                   
        """                                                                        
        :type head: ListNode                                                       
        :rtype: void Do not return anything, modify head in-place instead.         
        """   
        # 4 star，思路应该就是分成两个链表然后按要求合并
        if not head or head.next is None:                                          
            return                                                                 
        node = head                                                                
        index = 0                                                                  
        while node:                                                                
            node = node.next                                                       
            index += 1                                                             
        node = head                                                                
        i = 1                                                                      
        while i < (index+1) // 2:                                                  
            node = node.next                                                       
            i += 1                                                                 
        start = node.next                                                          
        node.next = None                                                           
        pre = None                                                                 
        node = start                                                               
        _start = None                                                              
        while node:                                                                
            next = node.next                                                       
            node.next =pre                                                         
            pre = node                                                             
            node = next                                                            
            if node is None:                                                       
                _start = pre                                                       
        node = head                                                                
        _node = _start                                                             
        while  node:                                                               
            next = node.next                                                       
            node.next = _node                                                      
            if _node:                                                              
                _next = _node.next                                                 
            else:                                                                  
                break                                                              
            node.next.next = next                                                  
            _node = _next                                                          
            node = next                                                            
                                                                                                                                                               
                                          
                                          
                                          
                                          
                                          
                                          
