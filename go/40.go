
//package main

import (
	"sort"
	//"fmt"
)
// 6 star, 同样是dfs的思想，不过需要注意避免重复，以及后续对切片的修改对之前切片的值的影响
func combinationSum2(candidates []int, target int) [][]int {
	var ret [][]int
	retP := &ret
	sort.Ints(candidates)
	dfs(candidates, target, 0, []int{}, retP)
	return *retP

}

func dfs(candidates []int, target int, curSum int, path []int, retP *[][]int) {
	if curSum == target {
		tempPath := make([]int, len(path))  //创建了切片的拷贝，避免后续的修改影响已加入结果集的切片的取值
		copy(tempPath, path)
		*retP = append(*retP, tempPath)
		return
	}
	for index, val := range candidates {
		if index == 0 || candidates[index] > candidates[index-1] { //避免重复
			if curSum + val > target {
				return
			} else {
				dfs(candidates[index+1:], target, curSum+val, append(path, val), retP)
			}

		}

	}
}


//func main() {
//	nums := []int {10, 1, 2, 7, 6, 1, 5}
//	ret := combinationSum2(nums, 8)
//	fmt.Println(ret)
//}