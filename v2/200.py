class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 6 star, no idea.
        # 思路：有一个二维列表来记录各个位置有没有被访问过，访问过的就直接跳过了，遍历存放数据的二维列表，对每一个位置上为1的点
        # 将其标注为已访问，然后向上下左右四个方向伸展，同样的，如果位置上为1被标注为已访问，这样一个岛屿的所有部分都会被扩展到，并且被标注
        # 然后将计数加1，继续遍历
        if not grid or not grid[0]:
            return 0
        column = len(grid[0])
        row = len(grid)
        visited = [[0 for _ in range(column)] for _ in range(row)]
        count = 0
        for i in range(row):
            for j in range(column):
                if not visited[i][j] and grid[i][j] == "1":
                    self.dfs(i, j, grid, visited)
                    count += 1
        return count

    def dfs(self, x, y, grid, visited):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != "1" or visited[x][y]:
            return
        visited[x][y] = 1
        self.dfs(x - 1, y, grid, visited)
        self.dfs(x, y - 1, grid, visited)
        self.dfs(x + 1, y, grid, visited)
        self.dfs(x, y + 1, grid, visited)


