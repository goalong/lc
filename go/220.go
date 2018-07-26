
package main

import (
	"math"
	//"fmt"
)

// 可以算是双指针法的变形，右指针从左到右遍历，左指针从右指针往前k个位置到右指针这段区间遍历，遍历时比较左右指针上的值的差是否小于t
func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	length := len(nums)
	for index:=1; index < length; index++ {
		left := index - k
		if left < 0 {left=0}
		for left < index {
			if math.Abs(float64(nums[left] - nums[index])) <= float64(t) {
				return true
			} else {
				left++
				}
		}
	}
	return false

}


//func main() {
//	nums := []int {1,2,3, 1}
//	ret := containsNearbyAlmostDuplicate(nums, 3, 0)
//	fmt.Println(ret)
//}