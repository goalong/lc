//
//package main
//import "fmt"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */


//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

// 6 star, queue存放当前层级的节点，nextLevel存放下一层级的节点，遍历queue,将其中的每个节点的左右节点放入nextLevel, 然后让
// queue=nextLevel, 开始遍历下一层的节点
func levelOrder(root *TreeNode) [][]int {
	if root == nil {return [][]int{}}
	var ret [][]int
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		temp := []int{}

		nextLevel := []*TreeNode{}
		for _, node := range queue {
			temp = append(temp, node.Val)
			if node.Left != nil {nextLevel = append(nextLevel, node.Left)}
			if node.Right != nil {nextLevel = append(nextLevel, node.Right)}


		}
		ret = append(ret, temp)
		queue = nextLevel
	}
	return ret

}


//func main() {
//	a := TreeNode{1, nil, nil}
//	b := TreeNode{2, nil, nil}
//	c := TreeNode{3, nil, nil}
//	a.Right = &b
//	a.Left = &c
//	fmt.Println(levelOrder(&a))
//}