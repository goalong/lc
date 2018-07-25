
package main

import "fmt"

func combinationSum3(k int, n int) [][]int {
	nums := []int {1, 2, 3, 4,5,6,7,8,9}
	var ret [][]int
	retP := &ret
	dfs(k, n, 0, nums, []int{}, retP)
	return *retP

}

func dfs(k int, n int, cur int, nums []int, path []int, retP *[][]int) {
	if k == 0 && cur == n {
		tempPath := make([]int, len(path))  //创建了切片的拷贝，避免后续的修改影响已加入结果集的切片的取值
		copy(tempPath, path)
		*retP = append(*retP, tempPath)
		return
	}
	for index, val := range nums {
		if k <= 0 {
			return
		} else {
			dfs(k-1, n, cur+val, nums[index+1:], append(path, val), retP)
		}
	}

}


func main() {
	ret := combinationSum3(3, 9)
	fmt.Println(ret)
}