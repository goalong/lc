//
//package main
//
//import "fmt"

// 5 star, 分为两种情况， nums[:-1]和nums[1:]
func rob(nums []int) int {
	length := len(nums)
	if length == 0 {
		return 0
	} else if length == 1 {
		return nums[0]
	} else if length == 2 {
		if nums[0] > nums[1] {
			return nums[0]
		} else {
			return nums[1]
		}
	}
	ret_a := helper(nums[:length-1])
	ret_b := helper(nums[1:])
	if ret_a > ret_b {
		return ret_a
	} else {
		return ret_b
	}

}


func helper(nums []int) int {
	length := len(nums)
	if length == 0 {
		return 0
	} else if length == 1 {
		return nums[0]}
	dp := make([]int, length)
	dp[0] = nums[0]
	if nums[1] > nums[0] {
		dp[1] = nums[1]
	} else {
		dp[1] = nums[0]
	}
	for i:=2; i< length; i++ {
		if dp[i-2] + nums[i] > dp[i-1] {
			dp[i] = dp[i-2] + nums[i]
		} else {
			dp[i] = dp[i-1]
		}
	}
	return dp[length-1]
}


//func main() {
//	fmt.Println(rob([]int{0, 0}))
//}
