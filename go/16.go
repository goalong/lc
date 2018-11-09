//package main
//
//import (
//	"math"
//	"sort"
//)

// 也很巧妙，6 star
// 思路同3sum，从左到右遍历，然后对后面的从两边往中间进行逼近，每次比较当前的和目前最接近的和谁更接近
// 然后按照当前和和目标值的相对大小调整左右的索引
func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	length := len(nums)
	gap := nums[0] + nums[1] + nums[2]

	for index, _ := range nums {
		if index == 0 || nums[index] > nums[index-1] {
			left, right := index+1, length-1
			for left < right {
				curSum := nums[index] + nums[right] + nums[left]
				if math.Abs(float64(curSum-target)) < math.Abs(float64(gap-target)) {
					gap = curSum
				}
				if curSum > target {
					right -= 1
				} else if curSum < target {
					left += 1
				} else {
					return curSum
				}
			}
		}

	}
	return gap

}

//func main() {
//	threeSumClosest([]int{0, 0, 0}, 1)
//
//}
