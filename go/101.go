
package main


// 6 star, 没想出来，必须熟练掌握
func isSymmetric(root *TreeNode) bool {
	return helper(root, root)

}

func helper(node1 *TreeNode, node2 *TreeNode) bool {
	 if node1 == nil && node2 == nil {return true}
	 if (node1 == nil && node2 != nil) || (node1 != nil && node2 == nil) {
	 	return false
	 }
	 if node1.Val != node2.Val {return false}
	 return helper(node1.Left, node2.Right) && helper(node1.Right, node2.Left)
}