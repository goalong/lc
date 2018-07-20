package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

//type ListNode struct {
//	Val int
//	Next *ListNode
//	}

// 2 star
//方法很简单直接，但是有许多边角情况需要处理，容易漏掉或出错
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var extra, current int
	var left *ListNode
	p1, p2 := l1, l2
	dummy := &ListNode{Val: 0, Next:nil}
	p := dummy
	for {
		if p1 == nil || p2 == nil {
			break
		} else {
			current = p1.Val + p2.Val + extra
			if current > 9 {
				extra = 1
				current = current - 10
			} else {
				extra = 0
			}
			p1 = p1.Next
			p2 = p2.Next
		}
		p.Next = &ListNode{Val: current, Next:nil}
		p = p.Next
	}
	if p1 != nil || p2 != nil {
		if p1 != nil {
			left = p1
		} else {
			left = p2
		}
		for {
			if left == nil {
				break
			}
			current = left.Val + extra
			if current > 9 {
				current -= 10
				extra = 1
			} else {
				extra = 0
			}
			p.Next = &ListNode{Val: current, Next:nil}
			p = p.Next
			left = left.Next
		}

	}
	if extra > 0 {
		p.Next = &ListNode{Val: extra, Next:nil}
	}
	return dummy.Next

}
