
package main

import "math"

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

// 6 star, 递归检测每个节点，一个节点的左子树的节点的值都在最小值和跟节点之间，右子数的所有节点的值都在跟节点和最大值之间
func isValidBST(root *TreeNode) bool {
	if root == nil {return true}
	return helper(root, math.MinInt64, math.MaxInt64)

}

func helper(node *TreeNode, min int, max int) bool {
	if node.Val <= min || node.Val >= max {
		return false
	}
	left, right := true, true
	if node.Left != nil {
		left = helper(node.Left, min, node.Val)
	}
	if node.Right != nil {
		right = helper(node.Right, node.Val, max)
	}
	return left && right
}