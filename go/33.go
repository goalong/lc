//package main
//import "fmt"


// 6 star, 二分法的变形，注意边界条件的检验，写错了很多次
//检查的时候，应该假设某一半是单调递增区间，然后让target在该区间为一种情况，不在该区间为一种情况

func search(nums []int, target int) int {
	var mid int
	length := len(nums)
	left, right := 0, length-1
	for left <= right {
		mid = (left+right)/2
		if nums[mid] == target {
			return mid
		}
		if nums[mid] >= nums[left] {
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
	return -1

}


//func main() {
//	nums := []int {4,5,6,7,8, 1,2,3}
//	fmt.Println(search(nums, 8))
//}