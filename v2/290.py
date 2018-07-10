
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # 5 star, 用一个字典记录每个字母和对应位置的单词，另一个字典记录单词和字母的映射
        # 如果出现同一个字母对应多个单词或者一个单词对应多个字母，则表明不匹配
        str_list = str.split(" ")
        if len(str_list) != len(pattern):
            return False
        letter_to_str = {}
        str_to_letter = {}
        for i, v in enumerate(pattern):
            if v not in letter_to_str:
                letter_to_str[v] = str_list[i]
            else:
                if letter_to_str[v] != str_list[i]:
                    return False

            if str_list[i] not in str_to_letter:
                str_to_letter[str_list[i]] = v
            else:
                if str_to_letter[str_list[i]] != v:
                    return False
        return True


# print(Solution().wordPattern("ab", "dog dog"))
