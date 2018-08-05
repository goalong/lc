package main

// 位运算，0 ^ 0 = 0
// n ^ 0 = n
// n ^ n = 0
func singleNumber(nums []int) int {
	num := 0
	for _, val := range nums {
		num ^= val
	}
	return num

}