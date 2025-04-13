# https://leetcode.com/problems/number-of-islands/description/
# https://www.workat.tech/problem-solving/practice/number-of-islands
# ./resources/009-number-of-islands.png
# Medium

# Problem:
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


# Approach:

# https://www.youtube.com/watch?v=gCswsDauXPc

def nums_of_islands(grid: list[list[int]]) -> int:

    row , col = len(grid), len(grid[0])
    total_islands = 0

    def dfs(i, j):
        if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0:
            return
        
        # mark the cell as 0, which means visited
        grid[i][j] = 0
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)



    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                total_islands += 1
                dfs(i, j)
    return total_islands

surface = [
 [1, 1, 0, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 1]
]

nums = nums_of_islands(surface)
print(nums)

