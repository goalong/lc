
//package main
//import "fmt"

//也是分别计算各个递增区间的收益，然后加起来就是最后的收益，从左到右遍历，根据当前的值和前边的值大小对比，比前面大则计算当前收益，并继续向前
//比前边小则将上个区间的收益加到总收益中，并更新start和curProfit的值，start是当前递增区间的起始值，curProfit是当前递增区间的收益
func maxProfit(prices []int) int {
	if len(prices) == 0 {return 0}
	profit, curProfit := 0, 0
	var start int
	for index,val := range prices {
		if index == 0 {
			start = val
			continue
			}
		if val >= prices[index-1] {
			curProfit = val - start
		} else {
			start = val
			profit += curProfit
			curProfit = 0
		}
	}
	profit += curProfit
	return profit
}

//func main() {
//	prices := []int{7,1,5,3,6,4}
//	//prices := []int {}
//	ret := maxProfit(prices)
//	fmt.Println(ret)
//}
