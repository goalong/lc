
package main
//
//import "fmt"

// 1 star
// slow, beat 2%, 可以改为使用二分法
func findPeakElement(nums []int) int {
	length := len(nums)
	if length == 1 {return 0}
	for index, _ := range nums {
		if index == 0 {
			if nums[index] > nums[index+1] {
				return index}
		} else if index == length-1 {
			if nums[index] > nums[index-1] {
				return index}
		} else {
			if nums[index] > nums[index-1] && nums[index] > nums[index+1] {
				return index
			}
		}
	}
	return 0
}


//func main() {
//	nums := []int {1}
//	fmt.Println(findPeakElement(nums))
//}