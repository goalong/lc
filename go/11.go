package main

// 从两边到中间移动，left,right代表左右的索引，每次的当前值等于height[left],height[right]中较小
//的值乘以（right-left), 然后用当前值将之前的值进行比较，并且对height[left]和height[right]较小的一个的索引向中间前进一位
func maxArea(height []int) int {
	var curAns, low, length int

	max := 0
	left, right := 0, len(height) - 1
	for left < right {
		length = right - left
		if height[left] > height[right] {
			low = height[right]
			right -= 1
		} else {
			low = height[left]
			left += 1
		}
		curAns = low * length
		if curAns > max {
			max = curAns
		}

	}
	return max
}

