package main

import (
	"sort"
	"fmt"
)

// 思路同3sum，先排序，之后两个for循环获得前两个元素，对后两个元素从左右两边往中间逼近来筛选，其中要注意防止重复
func fourSum(nums []int, target int) [][]int {
	var ret [][]int
	length := len(nums)
	sort.Ints(nums)
	for first:=0; first < length-3; first++ {
		if first == 0 || nums[first] > nums[first-1] {  //防止第一个元素重复
			for second:=first+1; second < length-2;second++ {
				if second == first+1 || nums[second] > nums[second-1] {  //防止第二个元素重复
					left, right := second+1, length-1
					for left < right {
						curSum := nums[first] + nums[second] + nums[left] + nums[right]
						if curSum > target {
							right--
						} else if curSum < target {
							left++
						} else {
							ret = append(ret, []int{nums[first], nums[second], nums[left], + nums[right]})
							left++
							for left <= right && nums[left] == nums[left-1] {left++}  //防止第三个元素重复，前三项不重复，第四项肯定不会重复了
						}

				}
				}
			}

		}

	}
	return ret

}


func main() {
	nums := []int {-3,-2,-1,0,0,1,2,3,3,3,3}
	ret := fourSum(nums, 0)
	fmt.Println(ret)

}