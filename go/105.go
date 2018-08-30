
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}



// 6 star, no idea
// 前序遍历，第一个值即为跟节点的值，然后在中序遍历的结果中找到根节点的索引，该索引前后即分别为二叉树的左右子树，递归执行
func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {return nil}
	root := TreeNode{preorder[0], nil, nil}
	rootIndex := index(inorder, root.Val)
	root.Left = buildTree(preorder[1:rootIndex+1], inorder[:rootIndex])
	root.Right = buildTree(preorder[rootIndex+1:], inorder[rootIndex+1:])
	return &root

}