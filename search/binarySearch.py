# 二分查找

# 二分搜索是一种在有序数组中查找某一特定元素的搜索算法。
# 搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；
# 如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。
# 如果在某一步骤数组为空，则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半。


def binary_search(iterable, start, end, target):
    if end >= start:
        mid = int(start + (end - start)/2)
        if iterable[mid] == target:
            return mid
        elif iterable[mid] > target:
            return binary_search(iterable, start, mid-1, target)
        else:
            return binary_search(iterable, mid+1, end, target)
    else:
        raise KeyError(f"{target} not in {iterable}")


if __name__ == '__main__':
    inter = range(0, 10, 2)
    try:
        result = binary_search(inter, 0, len(inter)-1, 4)
        print(f"元素在数组中的索引为{result}")
    except KeyError:
        raise
