//
//
//package main
//
//import "fmt"

func wordBreak(s string, wordDict []string) bool {
	length := len(s)
	dp := make([]bool, length+1)
	dict := make(map[string]string, len(wordDict))
	for _, word := range wordDict {
		dict[word] = ""
	}
	dp[0] = true
	for i := 1; i < length+1; i++ {
		for j:=0; j < i; j++ {
			_, ok := dict[s[j:i]]
			if dp[j] && ok {
				dp[i] = true
			}
		}
	}
	return dp[length]

}


//func main() {
//	fmt.Println(wordBreak("leetcode", []string{"leet", "code"}))
//}