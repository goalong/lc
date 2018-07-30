
package main
//
//import "fmt"

// 6 star, 用一个与nums等长的切片canArrive记录每个索引能否被跳到，从左到右遍历nums,根据每个索引上的步数更新canArrive上对应索引的值
//最后判断canArrive上最后一位的值是否为1
func canJump(nums []int) bool {
	var steps int
	canArrive := make([]int, len(nums))
	canArrive[0] = 1
	length := len(nums)
	index := 0
	for index < length && canArrive[index] == 1 {
		steps = nums[index]
		for idx:=1; idx<=steps;idx++{
			if index + idx >= length - 1 {return true}
			canArrive[index+idx] = 1
		}
		index += 1
	}
	return canArrive[length-1] == 1

}


//func main() {
//	nums := []int {2,3,1,1,4}
//	ret := canJump(nums)
//	fmt.Println(ret)
//}