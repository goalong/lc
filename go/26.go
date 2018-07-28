
package main

// 3 star, 双指针法，一个在前，一个在后，前面的遇到重复就略过，遇到不重复就更新到后面

func removeDuplicates(nums []int) int {
	fast, slow := 1, 1
	length := len(nums)
	for fast < length {
		if nums[fast] == nums[fast-1] {
			fast++
		} else {
			nums[slow] = nums[fast]
			slow++
			fast++
		}
	}
	return slow

}


//更简洁的
func removeDuplicates2(nums []int) int {
	if len(nums) <= 1 {
		return len(nums)
	}
	length := 1
	for k, v := range nums {
		if k > 0 && nums[length-1] != v {
			nums[length] = v
			length++
		}
	}
	return length
}

func main() {
	nums := []int {0,0,1,1,1,2,2,3,3,4}
	removeDuplicates(nums)
}