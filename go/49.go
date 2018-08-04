
package main

import (
	"sort"
	"strings"
)

// 使用一个map，key是每个排序后的字符串，值是相同字母组成字符串的数组
func groupAnagrams(strs []string) [][]string {
	var str string
	ret := [][]string{}
	strMap := make(map[string][]string)
	for _, val := range strs {
		str = sortString(val)
		_, ok := strMap[str]
		if ok {
			strMap[str] = append(strMap[str], val)

		} else {
			strMap[str] = []string{val}
		}
	}
	for _, sl := range strMap {
		ret = append(ret, sl)
	}
	return ret

}

func sortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}
