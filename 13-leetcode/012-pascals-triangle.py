# https://leetcode.com/problems/pascals-triangle/
# Easy

def solution(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    nums = [[1] * (i + 1) for i in range(numRows)]
    n = len(nums)
    for i in range(2, n):
        for j in range(1, i):
            nums[i][j] = nums[i-1][j-1] + nums[i-1][j]

    return nums


res = solution(5)
print(res)