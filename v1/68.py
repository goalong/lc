class Solution(object):
    def fullJustify(self, words, maxWidth):  # 1 star.
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        rs = []
        row = []
        for index, word in enumerate(words):
            row_len = sum([len(i) for i in row])
            if row_len + len(row) - 1 + len(word) <= maxWidth:
                row.append(word)
            else:
                avg_blank = (maxWidth - row_len) // (len(row) - 1)  # todo, not finish
                rs.append(row)
                row = [word]
        if row:
            rs.append(row)
        return rs


s = Solution()
print(s.fullJustify(
    ["This", "is", "an", "example", "of", "text", "justification."], 16))



        
