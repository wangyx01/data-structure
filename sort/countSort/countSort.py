# 计数排序

# 计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
# 作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数


def count_sort(array):
    output = [0 for _ in range(256)]

    count = [0 for _ in range(256)]

    ans = ["" for _ in array]

    for i in array:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(array)):
        output[count[ord(array[i])] - 1] = array[i]
        count[ord(array[i])] -= 1

    for i in range(len(array)):
        ans[i] = output[i]
    return ans


if __name__ == '__main__':
    array = "wwwrunoobcom"
    ans = count_sort(array)
    print("字符数组排序 %s" % ("".join(ans)))