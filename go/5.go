//package main
//
//import "fmt"

func longestPalindrome(s string) string {
	var ret1, ret2, maxByte, current string
	for index, _ := range s {
		ret1 = getLength(s, index, index)
		ret2 = getLength(s, index, index+1)
		if len(ret1) > len(ret2) {
			current = ret1
		} else {
			current = ret2
		}

		if len(current) > len(maxByte) {maxByte = current}
	}
	return string(maxByte)
}

// 核心是这个函数，left和right两个索引不断比较它们的值是否相同，如果相同就继续向两边扩展
func getLength(s string, left int, right int) string {
	for left >= 0 && right < len(s) {
		if s[left] == s[right] {
			left -= 1
			right += 1
		} else {
			break
		}

	}
	return s[left+1:right]
}


//func main() {
//	s := "cbbd"
//	a := longestPalindrome(s)
//	fmt.Println(a)
//}