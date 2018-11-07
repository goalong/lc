package main

import (
	"math"
	"fmt"
)

// 6 star, 运用一个切片记录各索引是否是素数，从最小的素数开始，逐个对它们的倍数标记为非素数，然后统计切片中素数的个数
func countPrimes(n int) int {
	if n < 3 {return 0}
	primeList := make([]int, n)
	for i, _ := range primeList {
		primeList[i] = 1
	}
	primeList[0], primeList[1] = 0, 0
	sqrt := int(math.Pow(float64(n), 0.5))+1
	for num:=2; num < sqrt; num++ {
		if primeList[num] == 1 {
			for index:=2*num; index < n; index+=num {
				primeList[index] = 0
			}
		}
	}
	count := 0
	for _, v := range primeList {
		if v == 1 {
			count++
		}
	}
	return count

}


func main() {
	fmt.Println(countPrimes(3))
}