# https://www.workat.tech/problem-solving/practice/collect-jewels

# ./resources/collect-jewels.png

# leecode：0/1 Knapsack Problem
# 
# https://github.com/itcharge/LeetCode-Py/blob/main/Contents/10.Dynamic-Programming/04.Knapsack-Problem/01.Knapsack-Problem-01.md

# https://www.youtube.com/watch?v=PfkBS9qIMRE

# Approach:


def collect_jewels(jewels: list[(int, int)], capacity: int) -> int:
    n = len(jewels)
    # 初始化 DP 数组
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 填充 DP 表
    for i in range(1, n + 1):
        weight, value = jewels[i - 1]
        for c in range(1, capacity + 1):
            if c >= weight:
                # 选择或不选择当前物品
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - weight] + value)
            else:
                # 当前物品不能选择
                dp[i][c] = dp[i - 1][c]

    # 返回最大价值
    return dp[n][capacity]

# 测试用例
jewels = [(1, 3), (2, 4), (3, 5), (4, 7)]
capacity = 5
print(collect_jewels(jewels, capacity))  # 输出: 10
