
package main

// 6 star, 利用中序遍历形成一个从小到大的顺序的性质

func kthSmallest(root *TreeNode, k int) int {
	nums := inorder(root, []int{})
	return nums[k-1]


}


func inorder(node *TreeNode, nums []int) []int {

	if node.Left != nil {
		nums = inorder(node.Left, nums)
	}
	nums = append(nums, node.Val)
	if node.Right !=  nil {
		nums = inorder(node.Right, nums)
	}
	return nums

}
