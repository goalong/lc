
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

func inorderTraversal(root *TreeNode) []int {
	if root == nil {return []int{}}
	var nums []int
	nums = inorder(root, nums)
	return nums

}


func inorder(node *TreeNode, nums []int) []int {

	if node.Left != nil {
		nums = inorder(node.Left, nums)
	}
	nums = append(nums, node.Val)
	if node.Right != nil {
		nums = inorder(node.Right, nums)
	}
	if node.Left == nil && node.Right == nil {
		return nums}
	return nums
}

//func main() {
//	a := TreeNode{1, nil, nil}
//	b := TreeNode{2, nil, nil}
//	c := TreeNode{3, nil, nil}
//	a.Right = &b
//	b.Left = &c
//	fmt.Println(inorderTraversal(&a))
//}