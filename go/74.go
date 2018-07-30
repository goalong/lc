
//package main

//import "fmt"

//todo, slow, beat 2%
//不断的与右上角位置的值进行比较，比右上角的大，则排除右上角所在行，否则，排除右上角所在列
func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 {return false}
	i, j := 0, len(matrix[0])-1
	for i < len(matrix) && j >= 0 {
		if target == matrix[i][j] {
			return true
		} else if target > matrix[i][j] {
			i++
		}else {
			j--
		}
	}
	return false

}


//func main() {
//	nums := make([][]int, 3)
//	nums[0] = []int{1,   3,  5,  7}
//	nums[1] = []int{10, 11, 16, 20}
//	nums[2] = []int{23, 30, 34, 50}
//
//	ret := searchMatrix(nums, 15)
//	fmt.Println(ret)
//}