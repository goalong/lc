
package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
// 6 star, 首先在s找到与t根节点的值相同的节点，如果找到开始递归检查是否值都相同与t相同
// 注意要把s 全部遍历了，因为只是一个二叉树，其任意一个子树都有可能(当然其实是高度相同的子树才有可能
func isSubtree(s *TreeNode, t *TreeNode) bool {
	if t == nil {return true}
	if s == nil {return false}
	if s.Val == t.Val {
		if isSame(s, t) {return true}
	}
	return isSubtree(s.Left, t) || isSubtree(s.Right, t)


}

// 检查a和两个树上每个位置的值是否都相同
func isSame(a *TreeNode, b *TreeNode) bool {
	if a == nil && b == nil {return true}
	if a == nil || b == nil {return false}
	if a.Val != b.Val {
		return false} else {
		return isSame(a.Left, b.Left) && isSame(a.Right, b.Right)
	}
}

func main() {
	a := TreeNode{1, nil, nil}
	b := TreeNode{2, nil, nil}
	c := TreeNode{3, nil, nil}
	d := TreeNode{4, nil, nil}
	e := TreeNode{5, nil, nil}

	d.Left = &a
	d.Right = &b
	c.Left = &d
	c.Right = &e
	fmt.Println(isSubtree(&c, &d))


}