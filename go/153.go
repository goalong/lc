
//package main

//import "fmt"

// 4 star, 二分法，不过比较的时候也有些巧妙
// 二分搜索法，即使旋转过了也会一半的任何一个元素始终比另一半的任何一个元素大，
// 所以如果nums[mid] < nums[high]，说明最小元素一定在[left, mid]中，所以令high = mid；
// 否则一定在[mid + 1, high]中，令low = mid + 1
func findMin(nums []int) int {
	var middle int
	left, right := 0, len(nums) - 1
	for left < right {
		middle = (left+right)/2
		if middle > 0 && nums[middle] < nums[middle-1] {
			return nums[middle]}
		if nums[middle] < nums[right] {
			right = middle
		} else {
			left = middle+1
		}


	}
	return nums[left]
}


//func main() {
//	nums := []int {1, 2}
//	fmt.Println(findMin(nums))
//}