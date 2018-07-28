package main

import (
	"math"
	"fmt"
)


//双指针法，左右两个索引，右索引从左到右遍历，当左右索引组成的区间的和大于等于s时，尝试将左索引向右移，获取以右索引为结尾的最小长度，
//用该最小长度与之前的最小长度做比较
func minSubArrayLen(s int, nums []int) int {
	var minLength, curSum int
	length := len(nums)
	left, right := 0, 0
	minLength = math.MaxInt64
	for right < length {
		if nums[right] >= s {return 1}
		curSum += nums[right]
		right++
		if curSum < s {
			continue
		} else {
			for curSum - nums[left] >= s {
				curSum -= nums[left]
				left++
			}
			if right - left < minLength {
				minLength = right - left
			}
		}

	}
	if minLength == math.MaxInt64 {
		return 0
	}
	return minLength
}


func main() {
	nums := []int {2,3,1,2,4,3}
	min := minSubArrayLen(7, nums)
	fmt.Println(min)
}