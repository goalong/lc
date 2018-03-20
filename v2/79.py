



class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 6 star, dfs
        # 遍历二维列表，找到第一个字符所在的位置，然后调用dfs函数，测试当前位置的上下左右是否等于下一个字符，注意将当前位置先标记为#，避免重复遍历
        def dfs(x, y, word):
            if not word:
                return True
            if x > 0 and board[x-1][y] == word[0]: # 向上
                temp = board[x][y]
                board[x][y] = "#"
                if dfs(x-1, y, word[1:]):
                    return True
                board[x][y] = temp
            if x < len(board) -1  and board[x+1][y] == word[0]: # 向下
                temp = board[x][y]
                board[x][y] = "#"
                if dfs(x+1, y, word[1:]):
                    return True
                board[x][y] = temp
            if y > 0 and board[x][y-1] == word[0]: # 向左
                temp = board[x][y]
                board[x][y] = "#"
                if dfs(x, y-1, word[1:]):
                    return True
                board[x][y] = temp
            if y < len(board[0]) - 1 and board[x][y+1] == word[0]: # 向右
                temp = board[x][y]
                board[x][y] = "#"
                if dfs(x, y+1, word[1:]):
                    return True
                board[x][y] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[1:]):
                        return True
        return False


