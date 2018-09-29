//package main
//
//import "fmt"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func flatten(root *TreeNode)  {
	if root == nil {return }
	var cur *TreeNode
	stack := []*TreeNode {root}
	prev := &TreeNode{0, nil, nil}
	for len(stack) > 0 {
		cur, stack = stack[len(stack)-1], stack[:len(stack)-1]
		if cur.Right != nil {
			stack = append(stack, cur.Right)
		}
		if cur.Left != nil {
			stack = append(stack, cur.Left)
		}
		prev.Left, prev.Right = nil, cur
		prev = cur

	}

}


//func main() {
//	a := TreeNode{1, nil, nil}
//	b := TreeNode{2, nil, nil}
//	c := TreeNode{3, nil, nil}
//	a.Right = &b
//	a.Left = &c
//	flatten(&a)
//	fmt.Println(a)
//}
//
