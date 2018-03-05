#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (34.73%)
# Total Accepted:    154.6K
# Total Submissions: 445.3K
# Testcase Example:  '[1,1,2]'
#
# 
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# 
# 
# For example,
# [1,1,2] have the following unique permutations:
# 
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
class Solution:                                                 
    def permuteUnique(self, nums):                              
        """                                                     
        :type nums: List[int]                                   
        :rtype: List[List[int]]                                 
        """   
        # 6 star, must master.
        nums.sort()                                             
        rs = []                                                 
        self.dfs([],nums, rs)                                   
        return rs                                               
    def dfs(self, path, nums, rs):                              
       if not nums:                                             
           rs.append(path)                                      
           return                                               
       pre = None                                               
       for i in range(len(nums)):                               
           if nums[i] == pre:                                   
               continue                                         
           pre = nums[i]                                        
           self.dfs(path+[nums[i]], nums[:i] + nums[i+1:], rs)  
                                                                
                                                                
