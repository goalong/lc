package main

import (
	"fmt"
	"sort"
)

// 一开始的思路还是for循环将其转换为2sum，但是这个解法不太好
//先排序，然后for循环遍历，对之后的部分进行首尾相加，如果结果大于0，则将右边的索引减1，
// 结果小于0则将左边索引加1，等于0则是想要的结果，注意要去除重复
func threeSum(nums []int) [][]int {
	var ret [][]int
	sort.Ints(nums)
	length := len(nums)
	for index, _ := range nums {
		if index == 0 || nums[index] > nums[index-1] {   //去除重复
			left, right := index+1, length - 1
			for left < right {
				cur_sum := nums[index] + nums[left] + nums[right]
				if cur_sum > 0 {
					right -= 1  // 这几处的去除错误很巧妙，起初写错了很多次
					for left <= right && nums[right] == nums[right+1] {right -= 1}
				} else if cur_sum < 0 {
					left += 1
					for left <= right && nums[left] == nums[left-1] {left += 1}
				} else {
					ret = append(ret, []int {nums[index], nums[left], nums[right]})
					left += 1
					for left <= right && nums[left] == nums[left-1] {
						left += 1}

				}
			}

		}

	}
	return ret

}


func main() {
	nums := []int {-1,0,1,0}
	//nums := []int {0,0,0,0,0,0,0,0,0,0,0,0}
	ret := threeSum(nums)
	fmt.Println(ret)
}