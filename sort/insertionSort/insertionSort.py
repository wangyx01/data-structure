# 插入排序

# 插入排序（Insertion Sort）是一种简单直观的排序算法。
# 它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入

def insertion_sort(iterable):

    for i in range(1, len(iterable)):
        key = iterable[i]
        j = i - 1
        while j >= 0 and key < iterable[j]:
            iterable[j+1] = iterable[j]
            j -= 1
        iterable[j+1] = key


if __name__ == '__main__':
    inter = [12, 1, 3, 11, 13, 5, 6]
    insertion_sort(inter)
    print(inter)
