
//package main
//
//import "fmt"

func partition(s string) [][]string {
	var ret [][]string
	dfs(s, []string{}, &ret)
	return ret

}


func isPalindrome(s string) bool {
	length := len(s)
	for i:=0; i < length/2 +1; i++ {
		if s[i] != s[length-1-i] {
			return false
		}
	}
	return true

}


func dfs(s string, path []string, ret *[][]string) {
	if s == "" {
		// 注意这里创建了一个新的切片，然后将path拷贝到新的切片中，然后把新的切片放到结果集中
		// 因为如果使用path这个切片，可能对影响到已经放入结果集的切片，因为切片共享一个底层数组
		temp := make([]string, len(path))
		copy(temp, path)
		*ret = append(*ret, temp)
		return
	}
	for i:=1; i < len(s)+1; i++ {
		if isPalindrome(s[:i]) {
			dfs(s[i:], append(path, s[:i]), ret)
		}
	}
}


//func main() {
//	s := "abababbaba"
//	ret := partition(s)
//	//fmt.Println(ret)
//	for i, _ := range ret {
//		fmt.Println(ret[i])
//	}
//}