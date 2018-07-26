
package main

import (
	"fmt"
	"math"
)

// 6 star, 这个也很巧妙，之前写错了几次，需要注意
func maxSubArray(nums []int) int {
	curSum, maxSum := -math.MaxInt64, -math.MaxInt64
	for _, val := range nums {
		if curSum <= 0 {
			curSum = val
		} else {
			curSum += val
		}
		if curSum > maxSum {maxSum = curSum}
	}

	return maxSum
}


func main() {
	//nums := []int {-2,1,-3,4,-1,2,1,-5,4}
	nums := []int {-8, 5}
	ret := maxSubArray(nums)
	fmt.Println(ret)
}