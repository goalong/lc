
package main

import "fmt"

// 从左到右遍历，start标记当前区间内的最小值，遇到下一个值比start小就更新start的值，遇到比start大就继续往前
// 在遍历中获取当前区间的最大收益，并且与之前的最大收益进行比较，比之前的大，则这就是新的最大收益
func maxProfit(prices []int) int {
	if len(prices) == 0 {return 0}
	start := prices[0]
	profit, curProfit := 0, 0
	for _,val := range prices[1:] {
		if val > start {
			curProfit = val - start
			if curProfit > profit {profit = curProfit}
		} else if val < start {
			start = val
		} else {continue}

	}
	return profit

}


func main() {
	//prices := []int{7,1,5,3,6,4}
	prices := []int {}
	ret := maxProfit(prices)
	fmt.Println(ret)
}
