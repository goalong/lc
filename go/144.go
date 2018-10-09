//package main
//
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

//5 star, 前序遍历，先本身，再左，再右
func preorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	if root.Right == nil && root.Left == nil {
		return []int{root.Val}
	}
	var nums []int
	return preorder(root, nums)

}

func preorder(node *TreeNode, nums []int) []int {
	nums = append(nums, node.Val)

	if node.Left != nil {
		nums = preorder(node.Left, nums)
	}
	if node.Right != nil {
		nums = preorder(node.Right, nums)
	}
	return nums

}


// 非递归实现前序遍历，使用栈，先将根节点入栈，随后从栈中取出节点，如果该节点有右子树，将右子树入栈，如果该节点有左子树，将左子树入栈
func preorderTraversal2(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	stack := []*TreeNode{root}
	var result []int
	var node *TreeNode
	for len(stack) > 0 {
		node, stack = stack[len(stack)-1], stack[:len(stack)-1]
		result = append(result, node.Val)
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
		if node.Left != nil {
			stack = append(stack, node.Left)
		}

	}
	return result

}




//func main() {
//	a := TreeNode{1, nil, nil}
//	b := TreeNode{2, nil, nil}
//	c := TreeNode{3, nil, nil}
//	a.Right = &b
//	a.Left = &c
//	fmt.Println(preorderTraversal(&a))
//}
