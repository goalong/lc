package main

import (
	"bytes"
)

func lengthOfLongestSubstring(s string) int {
	var maxLen, curLen, index int

	length := len(s)
	if length > 0 {maxLen = 1; curLen = 1}
	s_bytes := []byte(s)
	left, right := 0, 1
	for right < length {
		if index = bytes.IndexByte(s_bytes[left:right], s_bytes[right]); index > -1 {
			curLen = right - left
			if curLen > maxLen {
				maxLen = curLen
			}
			left += index + 1
			if left >= right {right = left}
			curLen = 1
		} else {
			right += 1
			curLen = right - left
		}

	}
	if curLen > maxLen {
		maxLen = curLen
	}
	return maxLen

}


func lengthOfLongestSubstring2(s string) int {
	n:=len(s)
	if n <= 1 {
		return n
	}
	myMap:=make(map[string]int,0)
	max:=0
	start:=0
	for k,v := range s {
		c:=string(v)
		i,ok:=myMap[c]
		if ok && i>=start {
			start=i+1
		}
		myMap[c]=k
		if k-start+1 > max {
			max=k-start+1
		}
	}
	return max
}

//func main() {
//	s := "anviaj"
//	len := lengthOfLongestSubstring(s)
//	fmt.Println(len)
//
//}