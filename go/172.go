
//package main
//
//import "fmt"

//6 star,  0是由2*5得到，2足够，所有就是求有多少个5的因子,
//n = 128, 第一遍 n/5 得到 25， 有25个5的倍数， 25／5 =5 ，有5个25的倍数， 5／5 = 1， 有1个125的倍数
//结果就是25 + 5 + 1， 注意为什么不是25 + 5 * 2 + 3 * 1, 因为前边已经算上了，所以 5 和 1 都只是加一次

func trailingZeroes(n int) int {
	num := 5
	count := 0
	for n >= num {
		count += n / num
		num *= 5
	}
	return count

}


//func main() {
//	fmt.Println(trailingZeroes(128))
//}