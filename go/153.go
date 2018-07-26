
package main

//import "fmt"

// 4 star, 二分法，不过比较的时候也有些巧妙
// 有点慢，beat 4%
func findMin(nums []int) int {
	var middle int
	left, right := 0, len(nums) - 1
	for left < right {
		middle = (left+right)/2
		if middle > 0 && nums[middle] < nums[middle-1] {
			return nums[middle]}
		if nums[right] > nums[left] {
			right = middle
		} else {
			if nums[middle] < nums[right] {
				right = middle
			} else {
				left = middle+1
			}

		}

	}
	return nums[left]
}


//func main() {
//	nums := []int {1, 2}
//	fmt.Println(findMin(nums))
//}