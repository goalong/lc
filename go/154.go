
//package main
//
//import "fmt"

// 6 star, 二分法，思路同153，只是当有相等时将边界收缩一下
func findMin(nums []int) int {
	length := len(nums)
	left, right := 0, length-1
	for left < right {
		mid := (left+right)/2
		if mid > 0 && nums[mid] < nums[mid-1] {
			return nums[mid]
		}
		if nums[mid] < nums[right] {
			right = mid
		} else if nums[mid] > nums[right] {
			left = mid + 1
		} else {
			right--
		}
	}
	return nums[left]

}

//func main() {
//	nums := []int{1, 1}
//	fmt.Println(findMin(nums))
//}