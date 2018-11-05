package main


func lengthOfLongestSubstring(s string) int {
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