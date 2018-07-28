
package main

// 3 star, 类似第26题，只是加一个变量考虑重复的次数
func removeDuplicates(nums []int) int {
	length := len(nums)
	if length <= 1 {return length}
	count := 1
	realLength := 1
	for index, val := range nums {
		if index > 0 && nums[index] != nums[index-1] {
			count = 1
			nums[realLength] = val
			realLength++
		} else if index > 0 && nums[index] == nums[index-1]{
			if count < 2 {
				nums[realLength] = nums[index]
				count++
				realLength++
			}

		}
	}
	return realLength


}


func main() {
	nums := []int{1,1,1,2,2,3}
	removeDuplicates(nums)
}