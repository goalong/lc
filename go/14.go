
package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {return ""}
	index := 0
	for {
		for _, str := range strs {
			if index >= len(str) {
				return str[:index]
			} else if str[index] == strs[0][index]{
				continue

			} else {
				return str[:index]
			}
		}
		index += 1
	}

}


func main() {
	strs := []string {"flower","flow","flight"}
	rs := longestCommonPrefix(strs)
	fmt.Println(rs)
}