//package main

import (
	//"fmt"
	"math"
)

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

// 5 star
func isBalanced(root *TreeNode) bool {
	var leftHeight, rightHeight int
	if root == nil || (root.Left == nil && root.Right == nil) {
		return true
	}
	if root.Left != nil {
		leftHeight = getHeight(root.Left) + 1
	}
	if root.Right != nil {
		rightHeight = getHeight(root.Right) + 1
	}

	if math.Abs(float64(leftHeight)-float64(rightHeight)) > 1.0 {
		return false
	}
	return isBalanced(root.Left) && isBalanced(root.Right)

}

//func getHeight(node *TreeNode) int {
//	var leftHeight, rightHeight int
//	if node == nil {
//		return 0
//	}
//	if node.Left != nil {
//		leftHeight = getHeight(node.Left)
//	}
//	if node.Right != nil {
//		rightHeight = getHeight(node.Right)
//	}
//	if leftHeight > rightHeight {
//		return leftHeight + 1
//	} else {
//		return rightHeight + 1
//	}
//}


func getHeight(node *TreeNode) int {
	var leftHeight, rightHeight int
	if node.Left == nil && node.Right == nil{
		return 0
	}
	if node.Left != nil {
		leftHeight = getHeight(node.Left) + 1
	}
	if node.Right != nil {
		rightHeight = getHeight(node.Right) + 1
	}
	if leftHeight > rightHeight {
		return leftHeight
	} else {
		return rightHeight
	}
}



//func main() {
//	a := TreeNode{1, nil, nil}
//	b := TreeNode{2, nil, nil}
//	c := TreeNode{3, nil, nil}
//	a.Right = &b
//	b.Right = &c
//	fmt.Println(isBalanced(&a))
//	//fmt.Println(getHeight(&a))
//}
