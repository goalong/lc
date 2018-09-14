
package main


type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 6 star, 数组的中间位置的值作为根节点，左节点为左半边数组的中间节点，右节点同理，递归
func sortedArrayToBST(nums []int) *TreeNode {
	length := len(nums)
	if length == 0 {return nil}
	if length == 1 {return &TreeNode{nums[0], nil, nil}}
	mid := length / 2
	node := TreeNode{nums[mid], nil, nil}
	left := sortedArrayToBST(nums[:mid])
	right := sortedArrayToBST(nums[mid+1:])
	node.Left, node.Right = left, right
	return &node

}