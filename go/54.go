//package main
//
//import "fmt"

// 不断变更matrix，每次依次按四个方向取出一行或一列加到结果的切片上
func spiralOrder(matrix [][]int) []int {
	var last, temp []int
	var first int
	//cols := len(matrix)
	//rows := len(matrix[0])
	ret := []int{}
	for len(matrix) > 0 {
		if len(matrix[0]) > 0 {
			ret = append(ret, matrix[0]...)  //切片后面追加一个切片
			matrix = matrix[1:]
		}
		if len(matrix) > 0 && len(matrix[0]) > 0 {
			for index,_ := range matrix {
				ret = append(ret, matrix[index][len(matrix[index])-1])
				matrix[index] = matrix[index][:len(matrix[index])-1]
			}
		}
		if len(matrix) > 0 {
			last = matrix[len(matrix)-1]
			last = reverse(last)
			ret = append(ret, last...)
			matrix = matrix[:len(matrix)-1]

		}

		if len(matrix) > 0 && len(matrix[0]) > 0 {
			temp = []int{}
			for i,_ := range matrix {
				first = matrix[i][0]
				temp = append(temp, first)
				matrix[i] = matrix[i][1:]
			}
			temp = reverse(temp)
			ret = append(ret, temp...)
		}

	}
	return ret

}


func reverse(nums []int) []int {
	for i:=0; i<len(nums)/2; i++ {
		opp := len(nums)-1-i
		nums[i], nums[opp] = nums[opp], nums[i]
	}
	return nums
}

//func main() {
//	nums := make([][]int, 3)
//	nums[0] = []int{1,2,3}
//	nums[1] = []int{4,5,6}
//	nums[2] = []int{7,8,9}
//
//	ret := spiralOrder(nums)
//	fmt.Println(ret)
//
//
//}