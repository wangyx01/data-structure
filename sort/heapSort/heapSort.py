# 堆排序

# 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
# 堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
# 堆排序可以说是一种利用堆的概念来排序的选择排序。

def heapify(array, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and array[i] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # 交换

        heapify(array, n, largest)


def heap_sort(array):
    n = len(array)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(array, n, i)

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # 交换
        heapify(array, i, 0)


if __name__ == '__main__':
    array = [12, 11, 13, 5, 6, 7]
    heap_sort(array)
    print(array)
