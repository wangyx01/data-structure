# 归并排序

# 归并排序（Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。
# 该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

# 分治法:
#     1. 分割：递归地把当前序列平均分割成两半。
#     2. 集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。


def merge(array, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # 创建临时数组
    L = [0] * n1
    R = [0] * n2

    # 拷贝数据到临时数组 arrays L[] 和 R[]
    for i in range(n1):
        L[i] = array[left + i]

    for j in range(n2):
        R[j] = array[mid + 1 + j]

    # 归并临时数组到 array[l..r]
    i = 0  # 初始化第一个子数组的索引
    j = 0  # 初始化第二个子数组的索引
    k = left  # 初始归并子数组的索引

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    # 拷贝 L[] 的保留元素
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    # 拷贝 R[] 的保留元素
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort(array, left, right):
    if left < right:
        mid = int((left + (right - 1)) / 2)
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)


if __name__ == '__main__':

    array = [12, 11, 13, 5, 6, 7, 8]
    merge_sort(array, 0, len(array)-1)
    print(array)
