package main

import "fmt"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 5 star, 前序遍历，先本身，再左，再右
func preorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	if root.Right == nil && root.Left == nil {
		return []int{root.Val}
	}
	var nums []int
	return preorder(root, nums)

}

func preorder(node *TreeNode, nums []int) []int {
	nums = append(nums, node.Val)

	if node.Left != nil {
		nums = preorder(node.Left, nums)
	}
	if node.Right != nil {
		nums = preorder(node.Right, nums)
	}
	return nums

}



func main() {
	a := TreeNode{1, nil, nil}
	b := TreeNode{2, nil, nil}
	c := TreeNode{3, nil, nil}
	a.Right = &b
	a.Left = &c
	fmt.Println(preorderTraversal(&a))
}
