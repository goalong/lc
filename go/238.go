package main


//使用两个切片分别记录各个索引左边的乘积和右边的乘积，然后相乘
//left[i]：存放nums[i]之前的乘积
//right[i]：存放nums[i]之后的乘积
func productExceptSelf(nums []int) []int {

	length := len(nums)
	left := make([]int, length)
	left[0] = 1
	right := make([]int, length)
	right[length-1] = 1
	for index:=1; index<length; index++ {
		left[index] = left[index-1] * nums[index-1]
	}

	for idx:=length-2; idx >= 0; idx-- {
		right[idx] = right[idx+1] * nums[idx+1]
	}
	for i, _ := range left {
		left[i] *= right[i]
	}
	return left

}

func main() {
	nums := []int {1,2,3,4}
	productExceptSelf(nums)
}