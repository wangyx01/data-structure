# 冒泡排序

# 冒泡排序（Bubble Sort）也是一种简单直观的排序算法。
# 它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
# 走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
# 这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端

def bubble_sort(iterable):

    for i in range(len(iterable)):

        # Last i elements are already in place
        for j in range(len(iterable)-i-1):

            if iterable[j] > iterable[j+1]:

                iterable[j], iterable[j+1] = iterable[j+1], iterable[j]


if __name__ == '__main__':
    A = [88, 89, 7, 6, 5, 3]
    bubble_sort(A)
    print(A)
