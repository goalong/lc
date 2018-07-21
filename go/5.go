package main

//import "fmt"

func longestPalindrome(s string) string {
	var byte1, byte2, maxByte, current []byte
	s_bytes := []byte(s)
	for index, _ := range s_bytes {
		byte1 = getLength(s_bytes, index, index)
		byte2 = getLength(s_bytes, index, index+1)
		if len(byte1) > len(byte2) {
			current = byte1
		} else {
			current = byte2
		}

		if len(current) > len(maxByte) {maxByte = current}
	}
	return string(maxByte)
}

// 核心是这个函数，left和right两个索引不断比较它们的值是否相同，如果相同就继续向两边扩展
func getLength(s_bytes []byte, left int, right int) []byte {
	length := len(s_bytes)
	for left >= 0 && right < length {
		if s_bytes[left] == s_bytes[right] {
			left -= 1
			right += 1
		} else {
			break
		}

	}
	return s_bytes[left+1:right]
}


//func main() {
//	s := "cbbd"
//	a := longestPalindrome(s)
//	fmt.Println(a)
//}