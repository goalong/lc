//
//package main
//
//import "fmt"

// 7 star, 未能想出来，难点在于发现规律，dp[i] = dp[0]*dp[i-1] + dp[1]*dp[i-2] + ... + dp[i-1]*dp[0]
// dp[i]表示i个数字的可以组成的独特的二叉查找树的个数，左边0个右边i-1个，左边1个右边i-2个，一直到到左边i-1个右边0个，这些情况的总和即是dp[i]
func numTrees(n int) int {
	dp := make([]int, n+1)
	dp[0], dp[1] = 1, 1
	for i := 2; i<n+1; i++ {
		for j:=0; j<i; j++ {
			dp[i] += dp[j] * dp[i-1-j]
		}
	}
	return dp[n]

}


//func main() {
//	fmt.Println(numTrees(3))
//}
