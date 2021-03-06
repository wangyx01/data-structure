# 选择排序

# 选择排序（Selection sort）是一种简单直观的排序算法。
# 它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 以此类推，直到所有元素均排序完毕

def selection_sort(iterable):
    for i in range(len(iterable)):
        min_index = i
        for j in range(i+1, len(iterable)):
            if iterable[min_index] > iterable[j]:
                min_index = j
        iterable[i], iterable[min_index] = iterable[min_index], iterable[i]


if __name__ == '__main__':
    A = [9, 1, 10, 7, 6, 8, 9]
    selection_sort(A)
    print(A)

