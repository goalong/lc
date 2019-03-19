class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # 7 star, 比较难，这道题立即想到用dfs,结果超时了，而且用dfs还有两处细节需要注意，一个是dfs中for循环的范围，一个是递归调用时path的赋值应该直接在调用中进行，如果单独写一行path.append(s[:i])，就是错误，因为list的可变性

#         result = []
#         path = []
#         memo = {}
#         self.dfs(s, set(wordDict), path, result, memo)
#         return result

#     def dfs(self, s, word_set, path, result, memo):
#         if s in memo:
#             return memo[s]
#         if s == "":
#             sentence = " ".join(path)
#             result.append(sentence)
#             return
#         for i in range(1, len(s)+1):
#             if s[:i] in word_set:
#                 self.dfs(s[i:], word_set, path + [s[:i]], result, memo)



print(Solution().wordBreak("catsanddog",
["cat","cats","and","sand","dog"]))