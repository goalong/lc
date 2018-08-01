
//package main

import (
	//"fmt"
	"sort"
)


// 5 star, dfs, 去重比较巧妙
// slow, beat 0%, 8ms
func subsetsWithDup(nums []int) [][]int {
	sort.Ints(nums)
	ret := [][]int{}
	retP := &ret
	dfs(retP, nums, []int{}, 0)
	return *retP


}

func dfs(retP *[][]int, nums []int, path []int, start int) {
	temp := make([]int, len(path))
	copy(temp, path)
	*retP = append(*retP, temp)
	if len(nums) == 0 {return}
	for i:= start; i<len(nums); i++ {
		//fmt.Println(start, path)
		if i == start || nums[i] != nums[i-1] {  //注意去除重复
			dfs(retP, nums, append(path, nums[i]), i+1)
		}

	}
}

//func subsetsWithDup(nums []int) [][]int {
//	sort.Ints(nums)
//	res := [][]int{}
//	var dfs func(int, []int)
//	dfs = func(index int, tmp []int) {
//		t := make([]int, len(tmp))
//		copy(t, tmp)
//		res = append(res, t)
//
//		for i := index; i < len(nums); i++ {
//			if i == index || nums[i] != nums[i-1] {
//				dfs(i+1, append(tmp, nums[i]))
//			}
//		}
//	}
//
//	dfs(0, make([]int, 0, len(nums)))
//	return res
//}

//func main() {
//	nums := []int {1,2,2}
//	fmt.Println(subsetsWithDup(nums))
//}
