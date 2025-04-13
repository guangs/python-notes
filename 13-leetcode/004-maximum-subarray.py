# https://leetcode.com/problems/maximum-subarray/description/
# Medium
# https://www.workat.tech/problem-solving/practice/largest-contiguous

#  ./resources/004-medium-maximum-subarray.png

# https://www.youtube.com/watch?v=hLPkqd60-28


# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


def solution(nums: list[int]) -> int:
    max_sum = nums[0]
    cur_sum = 0
    final_left = 0
    final_right = 0

    for right, num in enumerate(nums):
        if cur_sum < 0:
            cur_sum = 0
            final_left = right
        cur_sum += num
        if cur_sum > max_sum:
            final_right = right
        max_sum = max(max_sum, cur_sum)
    print(final_left, final_right)
    return max_sum


def solution2(nums: list[int]) -> int:
    max_sum = float('-inf')
    cur_sum = 0
    for _, num in enumerate(nums):
        cur_sum += num
        max_sum = max(max_sum, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return max_sum


res = solution2([-2,1,-3,4,-1,2,1,-5,4])
print(res)