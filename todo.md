### 目标
重点题目重点攻克，对于每一题分别从复杂度，数据结构以及思路上进行分析，并争取提供多个解法。
### 3 star 以上的题目
* 3 最长的没有重复字符的字串

思路：   没有重复字符的子字符串为一个目标字符串，遍历所有字符，记录字符到索引的映射，如果一个字符在目标子串中且其下标比目标子串的起始下标大，则需要更新目标子串的起始下标，不断比较并获取最大的长度


Python:

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 6 star, 遍历字符串，使用字典记录每个字母到索引的映射
        rs, start = 0, 0
        memo = {}
        for index, v in enumerate(s):
            # 当前字母不在s[start:index]范围内，可以继续向前遍历
            if v not in memo or memo[v] < start:
                rs = max(rs, index + 1 - start)
            # 当前字母在s[start:index]有重复，新的起点从重复字母索引的下一位开始
            else:
                start = memo[v] + 1
            memo[v] = index
        return rs
```
Go:

```
func lengthOfLongestSubstring(s string) int {
    start := 0
    max := 0
    memo := make(map[string]int)
    for index := 0; index < len(s); index++ {
        c := string(s[index])
        val, ok := memo[c]
        if ok && val >= start {
            start = val + 1
        }
        memo[c] = index
        if index +1 - start > max {
            max = index +1 - start
        } 
        
    }
    return max
    
}
```



* 5
* 9
* 15
* 16
* 17
* 18
* 19
* 20
* 22
* 26
* 27
* 31
* 32
* 33
* 34
* 39
* 40
* 46
* 47
* 48
* 50
* 53
* 55
* 60
* 62
* 63
* 64
* 69
* 70
* 72
* 
