
//package main

import (
	"sort"
	//"fmt"
)

// 6 star,  这个dfs实现耗费了许久，主要是下面注释处的两处问题
func combinationSum(candidates []int, target int) [][]int {
	var ret [][]int
	retP := &ret
	sort.Ints(candidates)
	dfs(candidates, target, []int{}, 0, retP)
	return *retP
}


func dfs(candidates []int, target int, path []int, curSum int, retP *[][]int) {
	//fmt.Println(path, curSum)
	if curSum == target {
		tempPath := make([]int, len(path))
		copy(tempPath, path)
		*retP = append(*retP, tempPath)  // 注意这里，是将path拷贝到一个新的切片，然后加到结果retP中，
		// 如果直接加，会出现问题，会发现原来加进去的切片的值被修改，不是我们想要的切片值，
		// 估计是由于切片都是基于一个数组，后面对切片的修改修改了底层的数组，所以前面切片的取值也会变化
		return
	}
	for index, val := range candidates {
		if curSum + val <= target {
			// 这里又是奇怪的一处，path和curSum如果按下面注释的那样先计算，再调用，结果又不对, 会少了几个结果集，
			// 猜测是计算后的赋值影响了后来的调用，还不太清楚
			//curSum += val
			//path = append(path, val)
			//dfs(candidates[index:], target, path, curSum, retP)
			dfs(candidates[index:], target, append(path, val), curSum+val, retP)

		} else {break}
	}
}



//func main() {
//	nums := []int {2, 3,  7}
//	ret := combinationSum(nums, 18)
//	fmt.Println(ret)
//
//	//ret := [][]int {}
//	//s := []int {2,5}
//	//ret = append(ret, s)
//	//s[0] = 100
//	//s = append(s, 9)
//	//fmt.Println(ret, s)
//
//}