
// 4 star
func containsNearbyDuplicate(nums []int, k int) bool {
	numMap := make(map[int]int)
	for index, val := range nums {
		if idx, ok := numMap[val]; ok {
			if index - idx <= k {return true}
		}
		numMap[val] = index
	}
	return false

}