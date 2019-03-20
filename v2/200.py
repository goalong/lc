class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 6 star, 遍历整个二维数组，在每一个上面为1的点向四边探测，并将探测路径上为1的进行标记为已访问，然后数量加1, 需要注意边界条件

        if not grid or not grid[0]:
            return 0
        column = len(grid)
        row = len(grid[0])
        count = 0
        for i in range(column):
            for j in range(row):
                if grid[i][j] == "1":
                    grid[i][j] = "#"
                    self.mark(i, j, column - 1, row - 1, grid)
                    count += 1
        return count

    def mark(self, i, j, x, y, grid):
        if i > 0 and grid[i - 1][j] == "1":
            grid[i - 1][j] = "#"
            self.mark(i - 1, j, x, y, grid)
        if i < x and grid[i + 1][j] == "1":
            grid[i + 1][j] = "#"
            self.mark(i + 1, j, x, y, grid)
        if j > 0 and grid[i][j - 1] == "1":
            grid[i][j - 1] = "#"
            self.mark(i, j - 1, x, y, grid)
        if j < y and grid[i][j + 1] == "1":
            grid[i][j + 1] = "#"
            self.mark(i, j + 1, x, y, grid)



