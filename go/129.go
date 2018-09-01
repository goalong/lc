
package main


// 6 star, 典型的dfs, curSum每次要乘以10然后加上当前节点的值，如果遇到叶节点，将当前的值加到总和中
func sumNumbers(root *TreeNode) int {
	if root == nil {return 0}
	sum := 0
	sum = dfs(root, 0, sum)
	return sum

}


func dfs(node *TreeNode, curSum int, sum int) int {
	if node.Left == nil && node.Right == nil {
		curSum = curSum * 10 + node.Val
		sum += curSum
		return sum
	}
	if node.Left != nil {
		sum = dfs(node.Left, curSum*10+node.Val, sum)
	}
	if node.Right != nil {
		sum = dfs(node.Right, curSum*10+node.Val, sum)
	}
	return sum
	}
