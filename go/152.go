
//package main

//import "fmt"

// 6 star, no idea, 由于负负得正，所以负数的结果也要记录
// positive = max(num, positive * num, negative * num)
// negative = min(num, temp * num, negative * num)
// go里没有直接提供max min这样的函数，所以代码里写的比较冗长
func maxProduct(nums []int) int {
	var temp int
	positive, negative,  max := nums[0], nums[0], nums[0]
	for _, val:= range nums[1:] {
		positive *= val
		negative *= val
		if positive < negative {
			temp = positive
			positive = negative
			negative = temp
		}
		if positive < val {
			positive = val
		}
		if negative > val {
			negative = val
		}

		if positive > max {max = positive}
	}
	return max
}


//func main() {
//	nums := []int {2,3,-2,4}
//	ret := maxProduct(nums)
//	fmt.Println(ret)
//}