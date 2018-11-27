package main

import "fmt"

// 6 star, 非常巧妙
// 动态规划，dp[i]表示以s[i]结尾的字符串所能组成的合规的子字符串的最大长度
// 显然,对于s[i]是左括号而言，dp[i]=0, 如果s[i]是右括号，
// j := index - 1 - dp[index-1] 计算出了以s[i-1]结尾的子字符串的起始的前一个位置，
// 如果s[j]是左括号且j>=0, 说明dp[i] = dp[i-1]+2, 即加上了j和i这两个位置的字符，此时还需要
// 考虑dp[j-1], 如果j-1>0，则dp[i]的最终结果还要加上dp[j-1],因为dp[j-1]可能也大于0

func longestValidParentheses(s string) int {
	length := len(s)
	dp := make([]int, length)
	for index:=1; index < length; index++ {
		if string(s[index]) == ")" {
			j := index - 1 - dp[index-1]
			if j >= 0 && string(s[j]) == "(" {
				dp[index] = dp[index-1] + 2
				if j - 1 >= 0 {
					dp[index] += dp[j-1]
				}

			}

		}
	}
	max := 0
	for _, i := range dp {
		if i > max {
			max = i
		}
	}
	return max

}

func main() {
	ret := longestValidParentheses("()()))))()()(")
	fmt.Println(ret)

	m := make(map[string]string)
	fmt.Println("start")

	m["ha"] = "ha"
	m["he"] = "he"

	for k, v := range m {
		m[k+"hello"] = v
		fmt.Println(k, v)
	}
}
