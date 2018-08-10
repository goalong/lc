
//package main
//
//import "fmt"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// type ListNode struct {
// 	Val int
// 	Next *ListNode
//}
// 4 star,
func reverseList(head *ListNode) *ListNode {
	node := head
	var pre, next *ListNode
	for node != nil {
		next = node.Next
		node.Next = pre
		pre = node
		node = next
	}
	return pre

}

//func main()  {
//	a := &ListNode{1, nil}
//	b := &ListNode{2, nil}
//	c := &ListNode{3, nil}
//	a.Next = b
//	b.Next = c
//	d := reverseList(a)
//	fmt.Println(d)
//
//}
