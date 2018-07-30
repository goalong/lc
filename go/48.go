
//package main

func rotate(matrix [][]int)  {
	var tempSlice []int
	var temp int
	cols := len(matrix)
	//rows := len(matrix[0])
	for index:=0; index < cols/2; index++ {
		tempSlice = matrix[index]
		matrix[index] = matrix[cols-1-index]
		matrix[cols-1-index] = tempSlice
	}
	for i:=0; i<cols; i++ {
		for j:=0; j< i; j++ {
			temp = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = temp
		}
	}

}
