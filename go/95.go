
package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 7 star, 多次未能解决，因此给七星，重点关注
func generateTrees(n int) []*TreeNode {
	if n == 0 {return []*TreeNode{}}
	ret := dfs(1, n)
	return ret

}


//func dfs(nums []int, result []*TreeNode, root *TreeNode, node *TreeNode) []*TreeNode {
//	if len(nums) == 0 {
//		result = append(result, root)
//		return result
//	}
//	for index, val := range nums {
//		other := append(nums[:index], nums[index+1:]...)
//		if root == nil {
//			root = &TreeNode{val, nil, nil}
//			node = root
//			result = dfs(other, result, root, node)
//		} else if node.Val > val {
//			node.Left = &TreeNode{val, nil, nil}
//			node = node.Left
//			result = dfs(other, result, root, node)
//		} else {
//			node.Right = &TreeNode{val, nil, nil}
//			node = node.Right
//			result = dfs(other, result, root, node)
//		}
//	}
//	return result
//
//}

// todo，没写出来，确实比较精巧
func dfs(start, end int) []*TreeNode {
	if start > end {return []*TreeNode{nil}}
	ret := []*TreeNode{}
	for mid:=start; mid<end+1; mid++ {
		left := dfs(start, mid-1)
		right := dfs(mid+1, end)

		for _, l := range left {
			for _, r := range right {
				root := TreeNode{mid, nil, nil}
				root.Left, root.Right = l, r
				ret = append(ret, &root)
			}
		}

	}
	return ret
}

func main() {
	fmt.Println(generateTrees(3))
}