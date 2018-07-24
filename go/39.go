
//package main

import (
	"sort"
	//"fmt"
)

func combinationSum(candidates []int, target int) [][]int {
	var ret [][]int
	retP := &ret
	sort.Ints(candidates)
	dfs(candidates, target, []int{}, 0, retP)
	return *retP
}


func dfs(candidates []int, target int, pathP []int, curSum int, retP *[][]int) {
	//fmt.Println(pathP, curSum, *retP)
	if curSum == target {
		*retP = append(*retP, pathP)
		return
	}
	for index, val := range candidates {
		if curSum + val <= target {
			dfs(candidates[index:], target, append(pathP, val), curSum+val, retP)
		}
	}
}



//func main() {
//	nums := []int {2, 3, 6, 7}
//	ret := combinationSum(nums, 7)
//	fmt.Println(ret)
//
//}