
//package main

//计数排序，计算每个元素的个数
func sortColors(nums []int)  {
	count := make([]int, 3)
	for _, num := range nums {
		count[num] += 1
	}
	index := 0
	for idx, _ := range count {
		for count[idx] > 0 {
			nums[index] = idx
			index++
			count[idx] -= 1
		}
	}

}
