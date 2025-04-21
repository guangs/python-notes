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
    while i < j:
        if arr[i] < pivot:
            i += 1
            continue
        if arr[j] > pivot:
            j -= 1
            continue
        arr[i], arr[j] = arr[j], arr[i]
    arr[0], arr[j] = arr[j], arr[0]
    left = quick_sort(arr[:j])
    right = quick_sort(arr[j + 1:])
    return left + [arr[j]] + right


print(merge_sort([5,1,1,2,0,0]))
print(quick_sort([5,1,1,2,0,0]))