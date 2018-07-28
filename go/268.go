package main

// 1 star，很简单直接
func missingNumber(nums []int) int {
	n := len(nums)
	ret := 0
	for index:=0;index<n;index++ {
		ret += index + 1
		ret -= nums[index]

	}
	return ret

}