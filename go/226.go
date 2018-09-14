package main

// 5 star, 代码很简洁，但要充分理解

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {return nil}
	left, right := root.Left, root.Right
	root.Left, root.Right = right, left
	invertTree(root.Left)
	invertTree(root.Right)
	return root

}