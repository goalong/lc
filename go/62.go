//package main

import "fmt"


// 6 star, 动态规划，状态转移方程dp[i[[j] = dp[i-1][j] + dp[i][j-1],
//首先需要把dp的第一行和第一列全部置为1
func uniquePaths(m int, n int) int {
	dp := make([][]int, m)
	for i:=0; i<m; i++ {
		dp[i] = make([]int, n)
		dp[i][0] = 1
	}
	for j:=0; j<n; j++ {
		dp[0][j] = 1
	}
	for i:=1;i<m;i++ {
		for j:=1; j<n; j++ {
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
		}
	}
	return dp[m-1][n-1]

}


//func main() {
//	fmt.Println(uniquePaths(3, 7))
//}