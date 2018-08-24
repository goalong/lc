
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, sum int) [][]int {
	ret := [][]int{}
	if root == nil {return ret}
	ret = dfs(root, 0, sum, []int{}, ret)
	return ret

}

func dfs(node *TreeNode, curSum int, sum int, path []int, ret[][]int) [][]int{
	if node.Right == nil && node.Left == nil {
		curSum += node.Val
		path = append(path, node.Val)
		if curSum == sum {
			temp := make([]int, len(path)) // 注意，这里拷贝了一份路径，然后放入结果里
			copy(temp, path)
			ret = append(ret, temp)
		}
		return ret
	}
	if node.Left != nil {
		ret = dfs(node.Left, curSum+node.Val, sum, append(path, node.Val), ret)
	}
	if node.Right != nil {
		ret = dfs(node.Right, curSum+node.Val, sum, append(path, node.Val), ret)
	}
	return ret

}

