//package main

// 5 star, 用两个切片分别记录各行和列是否有0
func setZeroes(matrix [][]int)  {
	cols := make([]int, len(matrix))
	rows := make([]int, len(matrix[0]))

	for i, _ := range matrix {
		for j, _ := range matrix[0] {
			if matrix[i][j] == 0 {
				cols[i] = 1
				rows[j] = 1
			}
		}
	}

	for i, _ := range matrix {
		for j, _ := range matrix[0] {
			if cols[i] == 1 || rows[j] == 1 {
				matrix[i][j] = 0
			}
		}
	}



}