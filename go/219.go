
package main
// 4 star, 使用一个map记录值到索引的映射，当有重复的时候，检查它们索引的差，小于等于k则表明存在，大于k则更新该值的索引为新的索引
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