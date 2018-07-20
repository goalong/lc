package main

//import "fmt"

// 使用一个map记录值到索引的映射，遍历nums，如果target - val在中，则找到了，不在则记录到map中
func twoSum(nums []int, target int) []int {
	var num int
	memoMap := make(map[int]int)
	for index, val := range nums {
		num = target - val
		_, ok := memoMap[num]
		if ok {
			return []int {memoMap[num], index}
		} else {
			memoMap[val] = index
		}

	}
	return []int {}

}

//func main() {
//	s := []int {1, 3, 2, 5, 6}
//	rs := twoSum(s, 10)
//	fmt.Println(rs)
//}