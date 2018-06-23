#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (36.34%)
# Total Accepted:    161.1K
# Total Submissions: 443.3K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 11110110101100000000
# Answer: 1
# Example 2:
# 11000110000010000011
# Answer: 3
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution(object):
    def numIslands(self, grid):  # 4 star, dfs, no idea.
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i,j)
                    count += 1
        return count
    def dfs(self, grid, i, j):
        # 对于不在矩阵内的或者是位置上不是1的直接跳过
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        # 对于位置上是1的，将其标注为-1，并向上下左右四个方向递归调用，因此一个岛屿的整个部分会全部变成-1，并且被计数上算作一个
        grid[i][j] = '-1'
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j + 1)
