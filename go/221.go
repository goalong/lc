
//package main


// 6 star, 动态规划，
func maximalSquare(matrix [][]byte) int {
	cols := len(matrix)
	if cols == 0 {return 0}
	rows := len(matrix[0])

	dp := make([][]int, cols)
	var width, temp int
	for index, _ := range dp {
		dp[index] = make([]int, rows)
	}

	for i:=0; i<cols; i++ {
		for j:=0; j < rows; j++ {
			if i == 0 || j == 0 {
				if matrix[i][j] == '0' {
					dp[i][j] = 0
				} else {
					dp[i][j] = 1
					if dp[i][j] > width {width = dp[i][j]}
				}
			} else if matrix[i][j] == '0' {
				dp[i][j] = 0
			} else {
				temp = min([]int{dp[i-1][j], dp[i-1][j-1], dp[i][j-1]})
				dp[i][j] = temp + 1
				if dp[i][j] > width {width = dp[i][j]}
			}

		}
	}
	return width * width

}


func min(nums []int) int {
	minVal := nums[0]
	for _, v:= range nums {
		if v < minVal {
			minVal = v
		}
	}
	return minVal
}


