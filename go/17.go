
package main

import "fmt"

func letterCombinations(digits string) []string {
	var ret []string
	digits_list := []byte(digits)
	letterMap := map[string][]string{
		"1": []string{},
		"2":[]string{"a","b","c"},
		"3":[]string{"d","e","f"},
		"4":[]string{"g","h","i"},
		"5":[]string{"j","k","l"},
		"6":[]string{"m","n","o"},
		"7":[]string{"p","q","r", "s"},
		"8":[]string{"t","u","v"},
		"9":[]string{"w","x","y", "z"},
	}
	dfs(digits_list, "", ret, letterMap)
	return ret


}

func dfs(digits_list []byte, path string, ret []string, letterMap map[string][]string) {
	if len(digits_list) == 0 {
		ret = append(ret, path)
		return
	}
	letters := letterMap[string(digits_list[0])]
	for _, v := range letters {
		dfs(digits_list[1:], path + v, ret, letterMap)
	}

}


func main() {
	ret := letterCombinations("23")
	fmt.Println(ret)

}