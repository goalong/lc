
package main
import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
// 5 star
func postorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	if root.Right == nil && root.Left == nil {
		return []int{root.Val}
	}
	var nums []int
	return postorder(root, nums)

}



func postorder(node *TreeNode, nums []int) []int {


	if node.Left != nil {
		nums = postorder(node.Left, nums)
	}
	if node.Right != nil {
		nums = postorder(node.Right, nums)
	}
	nums = append(nums, node.Val)
	return nums

}

func main() {
	a := TreeNode{1, nil, nil}
	b := TreeNode{2, nil, nil}
	c := TreeNode{3, nil, nil}
	a.Right = &b
	a.Left = &c
	fmt.Println(postorderTraversal(&a))

}

