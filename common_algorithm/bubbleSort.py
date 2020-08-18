# coding=utf-8
"""
冒泡排序
依次比较相邻两数据，将大的放到后面
时间复杂度：O(N**2)
"""
def bubble_sort(alist):
    for j in range(len(alist)-1, 0, -1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

alist = [54,26,93,17,77,31,44,55,20]
bubble_sort(alist)
print(alist)
