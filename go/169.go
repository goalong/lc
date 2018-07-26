
package main

// 6 star, 解法比较巧妙，没能做出来，只想到 蛮力算法
// slow, beat 4%
func majorityElement(nums []int) int {
	var count, num int
	for _, val := range nums {
		if count == 0 {
			num = val
		}
		if num == val {
			count += 1
		} else {
			count -= 1
		}
	}
	return num
}