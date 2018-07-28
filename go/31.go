
package main

import (
	"sort"
	"fmt"
)

// 6 star，思路正确，但在细节上错误了好几次

// 观察一下134875，它的下个是135478, 从最后一位开始，如果它前边的比它大，则继续向前，如果它前边的比它小，则停止
//此时对应的就是索引在8的位置，它前一个是4比它小，需要变更的子数组是4875这一部分，需要更改的就是在4后面找一个最小的但比4大的数5，
//把5放到子数组的开头，然后对剩下的部分升序排列即可，得到5478，用5478替换原来4875那一部分
//注意的是有可能整个数字全是升序的，例如1234，这时手动调整后两个的位置即可，也有可能整个数组是倒序的，例如4321，这时需要对整个数组进行升序排列

func nextPermutation(nums []int)  {
	var index, idx int
	length := len(nums)
	if length == 1 {return}
	for index=length-1;index>0;index-- {
		if nums[index-1] >= nums[index] {
			continue
		} else {
			break
		}
	}
	if index == 0 {
		sort.Ints(nums)
		return
	} else if index == length - 1 {
		last := nums[index]
		nums[index] = nums[index-1]
		nums[index-1] = last
		return
	}
	for idx=index;idx<length;idx++ {
		if idx == length - 1 {break}
		if nums[idx] > nums[index-1] && nums[idx+1] <= nums[index-1] {
			break
		}

	}
	left := nums[idx]
	nums[idx] = nums[index-1]
	nums[index-1] = left
	sort.Ints(nums[index:])
}


func main() {
	nums := []int {2,3, 1}
	nextPermutation(nums)
	fmt.Println(nums)

}