//package main
//import "fmt"

// 6 star, 需要注意特殊情况
// 终点是二分之后，必然有一半是有序的，对target在有序的那一半比较是一种情况，在另一半是另一种情况
func search(nums []int, target int) bool {
	var mid int
	length := len(nums)
	left, right := 0, length-1
	for left <= right {
		mid = (left+right)/2
		if nums[mid] == target {
			return true
		}
		if nums[left] == nums[right] && nums[left] == nums[mid] { //特殊情况
			left++
			right--
		} else if nums[mid] >= nums[left] {
			if nums[mid] > target && target >= nums[left]{ // left到mid是单调递增, target是在left到mid的区间
				right = mid - 1
			} else {
				left = mid + 1
			}

		} else if nums[right] >= nums[mid] {
			if nums[right] >= target && target > nums[mid]{ // mid到right是单调 递增
				left = mid + 1
			} else {
				right = mid - 1
			}
		}
	}
	return false


}

//func main() {
//	nums := []int {2,5,6,0,0,1,2}
//	fmt.Println(search(nums, 3))
//
//}