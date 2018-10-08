
//package main


// 6 star, 动态规划
// dp[i]表示到第i天的最大收益, 

func maxProfit(prices []int) int {
	length := len(prices)
	if length == 0 {return 0}
	dp := make([]int, length)
	var minPrice = prices[0]
	for i:=1; i<length; i++ {
		if dp[i-1] > prices[i] - minPrice {
			dp[i] = dp[i-1]
		} else {
			dp[i] = prices[i] - minPrice
		}
		if prices[i] < minPrice {minPrice = prices[i]}

	}
	ret := dp[length-1]
	maxPrice := prices[length-1]


	for j := length-1; j > 0; j-- {
		if maxPrice - prices[j] + dp[j-1] > ret {ret = maxPrice - prices[j] + dp[j-1]}
		if prices[j] > maxPrice {maxPrice = prices[j]}

	}
	return ret

}


//func main() {
//	//prices := []int {1,2,4,2,5,7,2,4,9,0}
//}