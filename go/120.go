//package main


func minimumTotal(triangle [][]int) int {
	var min int
	length := len(triangle)
	dp := triangle[length-1]
	for i := length-2; i > -1; i-- {
		for j := 0; j < i+1; j++ {
			min = dp[j]
			if dp[j+1] < min {
				min = dp[j+1]
			}
			dp[j] = triangle[i][j] + min
		}
	}
	return dp[0]

}