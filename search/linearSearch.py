# 线性查找

# 线性查找指按一定的顺序检查数组中每一个元素，直到找到所要寻找的特定值为止

def search(iterable, target):
    for i in range(0, len(iterable)):
        if iterable[i] == target:
            return i
    raise KeyError(f"{target} not in {iterable}")


if __name__ == '__main__':
    inter = range(0, 100, 2)
    try:
        result = search(inter, 10)
        print(f"元素在数组中的索引为{result}")
    except KeyError:
        raise

