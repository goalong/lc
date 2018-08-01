
//package main
//
//import "fmt"


// 5 star, 典型的dfs, 但是beat9%, 较慢
func subsets(nums []int) [][]int {
	ret := [][]int{}
	retP := &ret
	dfs(retP, nums, []int{})
	return *retP


}

func dfs(retP *[][]int, nums []int, path []int) {
	temp := make([]int, len(path))
	copy(temp, path)
	*retP = append(*retP, temp)
	if len(nums) == 0 {return}
	for i,_ := range nums {
		dfs(retP, nums[i+1:], append(path, nums[i]))
	}
}


//func main() {
//	nums := []int {1,2,3}
//	fmt.Println(subsets(nums))
//}