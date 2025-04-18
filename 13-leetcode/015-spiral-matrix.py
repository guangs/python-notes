# https://leetcode.com/problems/spiral-matrix/description/

# this is implemented by myself
def spiral_order(matrix: list[list[int]]) -> list:
    m, n = len(matrix), len(matrix[0])
    spiral = []
    visited = [ [False] * n for _ in range(m) ]
    direction_loop = ['right', 'down', 'left', 'up']

    i, j = 0, 0
    while len(spiral) < m * n:
        next_direction = direction_loop.pop(0)
        direction_loop.append(next_direction)
        match next_direction:
            case "right":
                while 0 <= i < m and 0 <= j < n and not visited[i][j]:
                    spiral.append(matrix[i][j])
                    visited[i][j] = True
                    j += 1
                if j >= n or visited[i][j]:
                    j -= 1 # 退回来
                    i += 1 # 向下走
            case "down":
                while 0 <= i < m and 0 <= j < n and not visited[i][j]:
                    spiral.append(matrix[i][j])
                    visited[i][j] = True
                    i += 1
                if i >= m or visited[i][j]:
                    i -= 1 # 退回来
                    j -= 1 # 向左走
            case "left":
                while 0 <= i < m and 0 <= j < n and not visited[i][j]:
                    spiral.append(matrix[i][j])
                    visited[i][j] = True
                    j -= 1
                if j < 0 or visited[i][j]:
                    j += 1 # 退回来
                    i -= 1 # 向上走
            case "up":
                while 0 <= i < m and 0 <= j < n and not visited[i][j]:
                    spiral.append(matrix[i][j])
                    visited[i][j] = True
                    i -= 1
                if i < 0 or visited[i][j]:
                    i += 1 # 退回来
                    j += 1 # 向右走
            case _:
                break

    return spiral


# this is enhanced by AI
def spiral_order2(matrix: list[list[int]]) -> list[int]:
    m, n = len(matrix), len(matrix[0])
    spiral = []

    # 定义方向数组，分别表示右、下、左、上
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0  # 当前方向索引

    # 初始化访问状态矩阵
    visited = [[False] * n for _ in range(m)]

    # 起始位置
    i, j = 0, 0

    for _ in range(m * n):
        # 记录当前元素
        spiral.append(matrix[i][j])
        visited[i][j] = True

        # 计算下一个位置
        next_i = i + directions[direction_index][0]
        next_j = j + directions[direction_index][1]

        # 检查是否需要切换方向
        if not (0 <= next_i < m and 0 <= next_j < n and not visited[next_i][next_j]):
            direction_index = (direction_index + 1) % 4  # 顺时针切换方向
            next_i = i + directions[direction_index][0]
            next_j = j + directions[direction_index][1]

        # 更新当前位置
        i, j = next_i, next_j

    return spiral

numbers = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]



print(spiral_order(numbers))
print(spiral_order2(numbers))