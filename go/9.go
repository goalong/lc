//package main
//
//import (
//	"fmt"
//	//"strconv"
//)


//将数字转换为字节数组，然后从首尾两边逐一对比，如果首尾不同，则不是回文
//func isPalindrome(x int) bool {
//	str := strconv.Itoa(x)
//	var intArray = []byte(str)
//	left, right := 0, len(intArray) - 1
//	for left <= right {
//		if intArray[left] != intArray[right] {
//			return false
//		} else {
//			left += 1
//			right -= 1
//		}
//	}
//	return true
//}


func isPalindrome(x int) bool {
	if x < 0 {return false}
	div := 1
	for x / div >= 10 {
		div *= 10
	}

	for x > 0 {
		left := x/div
		right := x % 10
		if left != right {
			return false
		}
		x %= div
		x -= right
		x /= 10
		div /= 100
	}
	return true
}



//func main() {
//	rs := isPalindrome(121)
//	fmt.Println(rs)
//}