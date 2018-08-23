
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 5 star, 递归，左右节点的高度的较大值加1

func maxDepth(root *TreeNode) int {
	if root == nil {return 0}
	return max(maxDepth(root.Left), maxDepth(root.Right)) + 1

}

func max(a, b int) int {
	if a > b {return a}
	return b
}