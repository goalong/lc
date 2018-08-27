package main

func index(slice []int, item int) int {
	for i, _ := range slice {
		if slice[i] == item {
			return i
		}
	}
	return -1
}

// 6 star, no idea
// 后序遍历的最后一个为跟节点的值，而跟节点的值将中序遍历分为左右两个子树，在中序遍历中找到根节点的索引，其前面即左子树，后面即右子树，这样递归处理
func buildTree(inorder []int, postorder []int) *TreeNode {
	length := len(inorder)
	if length == 0 {return nil}
	root := TreeNode{postorder[length-1], nil, nil}
	idx := index(inorder, root.Val)
	root.Left = buildTree(inorder[:idx], postorder[:idx])
	root.Right = buildTree(inorder[idx+1:], postorder[idx:length-1])
	return &root

}