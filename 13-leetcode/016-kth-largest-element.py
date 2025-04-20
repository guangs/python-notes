# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Medium

import heapq


def find_kth_largest_solution1(nums: list[int], k: int) -> int:
    heap = []

    # 建堆，保持堆里面有k个元素，即最大的k个，那么最上面的就是kth最大的
    for num in nums:
        if len(heap) < k:
            # 堆里不够k个元素时，入堆
            heapq.heappush(heap, num)
        else:
            # 堆里够k个元素时，先入堆排序，其中最小的会在最上面，然后把最小的弹出来，这样堆里还剩k个元素
            heapq.heappushpop(heap, num)

    return heapq.heappop(heap)


def find_kth_largest_solution2(nums: list[int], k: int) -> int:

    # heapq默认是最小堆，为了实现最大堆，将原来的num去负数
    for i, num in enumerate(nums):
        nums[i] = -num

    # 建堆
    heapq.heapify(nums)

    # 弹出kth最小的元素，取反后就是最大的kth
    for _ in range(k-1):
        heapq.heappop(nums)

    kth_num = - heapq.heappop(nums)

    return kth_num



nums = [3,2,3,1,2,4,5,5,6]
k = 4

res = find_kth_largest_solution1(nums, k)
print(res)

res = find_kth_largest_solution2(nums, k)
print(res)