
package main

import "fmt"

// 两个解法，一个dfs，一个多层嵌套的for循环

//func letterCombinations(digits string) []string {
//	var ret, tempRet []string
//	var retP *[]string
//	digits_list := []byte(digits)
//	letterMap := map[string][]string{
//		"1": []string{},
//		"2":[]string{"a","b","c"},
//		"3":[]string{"d","e","f"},
//		"4":[]string{"g","h","i"},
//		"5":[]string{"j","k","l"},
//		"6":[]string{"m","n","o"},
//		"7":[]string{"p","q","r", "s"},
//		"8":[]string{"t","u","v"},
//		"9":[]string{"w","x","y", "z"},
//	}
//	if len(digits_list) == 0 {
//		return ret
//	} else {
//		for _, v := range letterMap[string(digits_list[0])] {
//			ret = append(ret, v)
//		}
//	}
//	for _, v := range digits_list[1:] {
//		letters := letterMap[string(v)]
//		for _, str := range ret {
//			for _,letter := range letters {
//				newStr := str + letter
//				tempRet = append(tempRet, newStr)
//			}
//		}
//		ret = tempRet
//		tempRet = []string{}
//
//	}
//	return ret
//
//}

func letterCombinations(digits string) []string {
	digits_list := []byte(digits)
	if len(digits_list) == 0 {return []string{}}
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
	ret := []string{}
	retP := &ret
	dfs(digits_list, "", retP, letterMap)
	return *retP

}


// todo  想用dfs，但没能实现，关键是无法保存变量 ret，
// 后来查到变量逃逸，想到用指针或许可以解决，没想到成功了
func dfs(digits_list []byte, path string, retP *[]string, letterMap map[string][]string) {
	if len(digits_list) == 0 {
		*retP = append(*retP, path)
		return
	}
	num := string(digits_list[0])
	letters := letterMap[num]
	for _, v := range letters {
		dfs(digits_list[1:], path + v, retP, letterMap)
	}

}


func main() {
	ret := letterCombinations("")
	fmt.Println(ret)

}