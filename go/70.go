//
//package main
//
//import "fmt"

func climbStairs(n int) int {
	if n < 2 {
		return n
	}
	dp := make([]int , n)
	dp[0], dp[1] = 1, 2
	for i:=2; i<n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}
	return dp[n-1]
}


//func main() {
//	n := 1
//	fmt.Println(climbStairs(n))
//
//}