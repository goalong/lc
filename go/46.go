package main

import (
	"fmt"
)

// todo,  6 star, 这个解答速度太慢，一千五百多毫秒
func permute(nums []int) [][]int {
	if len(nums) == 0 {return [][]int{}}
	result := &[][]int{}
	dfs(nums, []int{}, result)
	return *result

}


func dfs(nums []int, path []int, result *[][]int)  {
	fmt.Println(nums, path, *result)
	if len(nums) == 0 {
		tempPath := make([]int, len(path))
		copy(tempPath, path)
		*result = append(*result, path)
		return
	}
	for i, num := range nums {
		left := make([]int, len(nums))
		copy(left, nums)
		left = append(left[:i], left[i+1:]...)
		dfs(left, append(path, num), result)

		//dfs(append(nums[:i], nums[i+1:]...), append(path, num), result)   一开始这样写，但结果不对，
	}
}




func main() {
	nums := []int{1,2,3}
	fmt.Println(permute(nums))
}