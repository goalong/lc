
//package main

//import "fmt"

// 6 star, 动态规划
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if obstacleGrid[0][0] == 1 {return 0}
	cols := len(obstacleGrid)
	rows := len(obstacleGrid[0])
	dp := make([][]int, cols)
	for i:=0; i<cols; i++ {
		dp[i] = make([]int, rows)
		if i == 0 {dp[i][0] = 1}
		if (i > 0 && dp[i-1][0] == 0) || obstacleGrid[i][0] == 1 {
			dp[i][0] = 0
		} else {
			dp[i][0] = 1
		}

	}
	for j:=0; j<rows; j++ {
		if (j > 0 && dp[0][j-1] == 0) || obstacleGrid[0][j] == 1 {
			dp[0][j] = 0
		} else {
			dp[0][j] = 1
		}
	}
	for i:=1;i<cols;i++ {
		for j:=1; j<rows; j++ {
			if obstacleGrid[i][j] == 1{
				dp[i][j] = 0
			} else {
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
			}

		}
	}
	return dp[cols-1][rows-1]

}


//func main() {
//	nums := make([][]int, 3)
//	nums[0] = []int {0,0,0}
//	nums[1] = []int {0,1,0}
//	nums[2] = []int{0,0,0}
//	fmt.Println(uniquePathsWithObstacles(nums))
//
//}
