
package main

// 3 star, 使用两个map各自记录s和t相同位置的字母的映射，如果一个字母映射两个即不正确
func isIsomorphic(s string, t string) bool {
	var b byte
	map1 := make(map[byte]byte)
	map2 := make(map[byte]byte)
	byteS := []byte(s)
	byteT := []byte(t)

	for i, _ := range s {
		b = byteS[i]
		if _, ok := map1[b]; ok {
			if map1[b] != byteT[i] {return false}
		} else {
			map1[b] = byteT[i]
		}
		b = byteT[i]
		if _, ok:=map2[b]; ok {
			if map2[b] != byteS[i] {return false}
		} else {
			map2[b] = byteS[i]
		}

	}
	return true
}