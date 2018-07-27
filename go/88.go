package main

// 6 star, no idea
// 从最后面往前合并，最后一个是在索引m+n-1,比较两个数组的最后一个，更大的那个存储在最后一位，然后往前走
// 注意有可能nums1遍历完了但nums1还有剩余，这时要把剩余的全部补到nums1上
func merge(nums1 []int, m int, nums2 []int, n int)  {
	index := m+n-1
	for m > 0 && n > 0 {
		if nums1[m-1] > nums2[n-1] {
			nums1[index] = nums1[m-1]
			m--
		} else {
			nums1[index] = nums2[n-1]
			n--
		}
		index--
	}
	if n > 0 {
		for idx:=0; idx<n; idx++ {
			nums1[idx] = nums2[idx]
		}
	}

}