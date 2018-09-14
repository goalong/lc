
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 5 star, 按层次遍历，当前层的节点如果有一个是叶子，则当前层的深度即是最小深度

func minDepth(root *TreeNode) int {
	if root == nil {return 0}
	if root.Right == nil && root.Left == nil {return 1}
	queue := []*TreeNode{root}
	depth := 0
	for len(queue) > 0 {
		depth += 1
		nextLevel := []*TreeNode{}
		for _, node := range queue {
			if node.Left == nil && node.Right == nil {return depth}
			if node.Left != nil {nextLevel = append(nextLevel, node.Left)}
			if node.Right != nil {nextLevel = append(nextLevel, node.Right)}
		}
		queue = nextLevel
	}
	return depth


}