# https://leetcode.com/problems/sort-an-array/description/
# Medium


def merge_sort(arr: list[int]) -> list[int]:
    n = len(arr)

    if n <= 1:
        return arr

    m = n // 2
    l = arr[:m]
    r = arr[m:]

    sorted_l = merge_sort(l)
    sorted_r = merge_sort(r)

    sorted_arr = []
    i, j = 0, 0

    while i < len(sorted_l) and j < len(sorted_r):
        if sorted_l[i] <= sorted_r[j]:
            sorted_arr.append(sorted_l[i])
            i += 1
        else:
            sorted_arr.append(sorted_r[j])
            j += 1

    if i >= len(sorted_l):
        sorted_arr.extend(sorted_r[j:])
    if j >= len(sorted_r):
        sorted_arr.extend(sorted_l[i:])

    return sorted_arr



def quick_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr[0]
    i = 1
    j = n - 1
    while i <= j:
        if arr[i] < pivot:
            i += 1
            continue
        if arr[j] > pivot:
            j -= 1
            continue
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    arr[0], arr[j] = arr[j], arr[0]
    left = quick_sort(arr[:j])
    right = quick_sort(arr[j + 1:])
    return left + [arr[j]] + right


def insert_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(1, n): # 从第二个元素开始
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -=1
    return arr

def shell_sort2(arr: list[int]) -> list[int]:
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for k in range(gap): # 分组
            for i in range(k + gap, n, gap):  # 每组用插入排序
                j = i
                while j >= gap and arr[j] < arr[j-gap]:
                    arr[j], arr[j-gap] = arr[j-gap], arr[j]
                    j -= gap
        gap = gap // 2
    return arr
    
def shell_sort(arr: list[int]) -> list[int]:
    n = len(arr)

    gap = n // 2
    while gap > 0:
        for i in range(gap, n): # 上面的两个for循环可以简化为一个for循环
            j = i
            while j >= gap and arr[j] < arr[j-gap]: # 这里通过gap已经进行了分组
                arr[j], arr[j-gap] = arr[j-gap], arr[j]
                j -= gap
        gap = gap // 2
    return arr


print(merge_sort([10,7,8,9,1,5]))
print(quick_sort([10,7,8,9,1,5]))
print(insert_sort([10,7,8,9,1,5]))
print(shell_sort2([10,7,8,9,1,5]))
print(shell_sort([10,7,8,9,1,5]))