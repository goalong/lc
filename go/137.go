package main

import "fmt"

// 2 star, 用map记录每个数字的次数，然后遍历map找到次数为1的
func singleNumber(nums []int) int {
	m := make(map[int]int)
	for _, num := range nums {
		_, ok := m[num]
		if ok {
			m[num] += 1
		} else {
			m[num] = 1
		}
	}
	for k, v := range m {
		if v == 1 {return k}
	}
	return 0

}

func main() {
	nums := []int {0,1,0,1,0,1,99}
	fmt.Println(singleNumber(nums))
}