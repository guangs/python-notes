# https://leetcode.com/problems/maximum-subarray/description/
# Medium
# https://www.workat.tech/problem-solving/practice/largest-contiguous

#  ./resources/004-medium-maximum-subarray.png

# https://www.youtube.com/watch?v=hLPkqd60-28&t=222s


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

    left = 0
    max_sum = nums[0]
    current_sum = 0
    n = len(nums)

    for right in range(0, n):
        if current_sum < 0:
            left = right
            current_sum = 0
        current_sum += nums[right]
        max_sum = max(max_sum, current_sum)
    return max_sum
