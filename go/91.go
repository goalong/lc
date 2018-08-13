

//package main

import (
	"strconv"
	//"fmt"
)
// 6 star, 动态规划，需要分类讨论，每相邻两个字符串组成的数组，如果在11到26之间且不等于20，则dp[i] = dp[i-1] + dp[i-2]
// 如果是10或20，则dp[i] = dp[i-2], 如果大于26且末尾是0，例如30 40， 则dp[i] = 0, 如果大于26且末尾不是0，则dp[i]=dp[i-1]
func numDecodings(s string) int {
	if s == "" || string(s[0]) == "0" {return 0}
	length := len(s)
	dp := make([]int, length+1)
	dp[0], dp[1] = 1, 1
	for i:=2; i < length + 1; i++{
		cur, _ := strconv.Atoi(s[i-2:i])
		if cur <= 26 && cur > 10 && cur != 20 {
			dp[i] = dp[i-1] + dp[i-2]
		} else if cur == 10 || cur == 20 {
			dp[i] = dp[i-2]
		} else {
			if before, _ := strconv.Atoi(string(s[i-1])); before != 0 {  // 排除cur是70 80这一类情况
				dp[i] = dp[i-1]
			}

		}
	}
	return dp[length]

}


//func main() {
//	fmt.Println(numDecodings("100"))
//}
