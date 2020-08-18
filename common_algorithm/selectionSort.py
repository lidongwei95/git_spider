#coding=utf-8
"""
选择排序：
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
时间复杂度：O(N**2)
"""
def selection_sort(alist):
	n = len(alist)
	for i in range(n-1):
		min_index = i
		for j in range(i+1, n):
			if alist[j] < alist[min_index]:
				min_index = j
		if min_index != i:
			alist[i], alist[min_index] = alist[min_index], alist[i]


alist = [54,226,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)
		