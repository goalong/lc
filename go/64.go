package main

import "fmt"

// 6 star, 动态规划，需要先计算最上和最左的行和列的值，其余的部分dp[i][j] = min(dp[i-1][j], dp[i][j-1], grid[i][j])
// 注意二维切片的初始化有些怪异
func minPathSum(grid [][]int) int {
	rows := len(grid[0])
	cols := len(grid)
	dp := make([][]int, cols)
	for c:=0; c<cols;c++ {
		dp[c] = make([]int, rows)  //初始化二维切片
	}
	dp[0][0] = grid[0][0]

	for index, val := range grid[0][1:] {
		dp[0][index+1] = dp[0][index] + val
	}
	for idx:=1; idx<cols; idx++ {
		dp[idx][0] = dp[idx-1][0] + grid[idx][0]
	}
	for i:=1; i < cols; i++ {
		for j:=1; j<rows; j++ {
			if dp[i-1][j] > dp[i][j-1] {
				dp[i][j] = dp[i][j-1] + grid[i][j]
			} else {
				dp[i][j] = dp[i-1][j] + grid[i][j]
			}
		}
	}
	return dp[cols-1][rows-1]

}


func main() {
	var nums [][]int
	nums = append(nums, []int{1,2,5})
	//nums = append(nums, []int{1,5,1})
	nums = append(nums, []int{3,2,1})
	ret := minPathSum(nums)
	fmt.Println(ret)
}