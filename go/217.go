package main

// 1 star, 很慢，可以看看别人的golang实现

func containsDuplicate(nums []int) bool {
	numMap := make(map[int]int)
	for _, val := range nums {
		if _, ok := numMap[val]; ok {
			return true
		} else {
			numMap[val] = 1
		}
	}
	return false

}