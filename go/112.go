
package main

import "github.com/astaxie/beego"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 6 star, 没写出来，需要重点掌握
// 如果当前节点是叶子节点，则检查当前的和和目标值是否相等，否则，检查左节点或右节点是否满足
func hasPathSum(root *TreeNode, sum int) bool {
	return checkSum(root, sum, 0)

}

func checkSum(node *TreeNode,  sum int, curSum int) bool {
	if node == nil {return false}
	curSum += node.Val
	if node.Left == nil && node.Right == nil && sum == curSum {
		return true
	}
	return checkSum(node.Left, sum, curSum) || checkSum(node.Right, sum, curSum)
}

