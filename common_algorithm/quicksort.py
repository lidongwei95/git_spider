# 快速排序，
# 原理：取出数据中的一个，将数据以该数据为基准分为两部分，
# 一部分大于该数据，另一部分小于该数，递归至只有一个数据
def quicksort(alist, start, end):
    if start >= end:
        return
    mid = alist[start]
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid

    quicksort(alist, start, low-1)
    quicksort(alist, low+1, end)

alist = [22, 44, 11, 25, 53, 95, 73, 23]
quicksort(alist, 0, len(alist)-1)
print(alist)
