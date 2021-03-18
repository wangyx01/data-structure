# 希尔排序

# 希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。

# 希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
# 待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。

def shell_sort(array):
    n = len(array)
    gap = int(n / 2)

    while gap > 0:

        for i in range(gap, n):

            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap = int(gap / 2)


if __name__ == '__main__':

    array = [12, 34, 54, 2, 3]
    shell_sort(array)
    print(array)
