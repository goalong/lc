

//package main

import (
	//"fmt"
	"strconv"
	"strings"
)

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

// 6 star, dfs
func binaryTreePaths(root *TreeNode) []string {
	if root == nil {return []string{}}
	var ret []string
	ret = dfs(root, []int{}, ret)
	return ret

}


func dfs(node *TreeNode, path []int, ret []string) []string {
	if node.Right == nil && node.Left == nil {
		path = append(path, node.Val)
		p := []string{}
		for _, s := range path {
			v := strconv.Itoa(s)
			p = append(p, v)
		}
		ret = append(ret, strings.Join(p, "->"))
		return ret

	}
	if node.Left != nil {


		ret = dfs(node.Left, append(path, node.Val), ret)
	}
	if node.Right != nil {
		ret = dfs(node.Right, append(path, node.Val), ret)
	}
	return ret
}

//func main() {
//	a := TreeNode{1, nil, nil}
//	b := TreeNode{2, nil, nil}
//	c := TreeNode{3, nil, nil}
//	d := TreeNode{4, nil, nil}
//	e := TreeNode{5, nil, nil}
//	a.Right = &b
//	a.Left = &c
//	c.Left = &e
//	b.Right = &d
//	fmt.Println(binaryTreePaths(&a))
//}