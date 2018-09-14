



class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 5 star
        # dfs, ac了但是很慢，看看更好的解法
        if digits == "":
            return []
        num_map = {
             '1': [],
             '2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']
             }
        rs = []
        path = ""
        self.dfs(digits, rs, path, num_map)
        return rs


    def dfs(self, digits, rs, path, num_map):
        if digits == "":
            rs.append(path)
            return
        chars = num_map.get(digits[0], [])
        for char in chars:
            self.dfs(digits[1:], rs, path+char, num_map)
