package main

import (
	"sort"
	"strings"
)

// 比较两个字符串排序后的结果是否相同
func isAnagram(s string, t string) bool {
	sortedS := sortString(s)
	sortedT := sortString(t)
	return sortedS == sortedT

}

func sortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}
