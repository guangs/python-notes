# https://leetcode.com/problems/rotating-the-box/description/
# Medium

# https://www.youtube.com/watch?v=LZr1w0LVzFw



def rotate_box_clockwise_90(box: list[list[str]]) -> list[list[str]]:
    row, col = len(box), len(box[0])
    rotated_box = []
    for i in range(col):
        rotated_box.append([])
        for j in range(row):
            rotated_box[i].append(box[-j-1][i])
    print('rotate_box_clockwise_90')
    return rotated_box


def rotate_box_clockwise_180(box: list[list[str]]) -> list[list[str]]:
    row, col = len(box), len(box[0])
    rotated_box = []
    for i in range(row):
        rotated_box.append([])
        for j in range(col):
            rotated_box[i].append(box[-i-1][-j-1])
    print('rotate_box_clockwise_180')
    return rotated_box


def rotate_box_counterclockwise_90(box: list[list[str]]) -> list[list[str]]:
    row, col = len(box), len(box[0])
    rotated_box = []
    for i in range(col):
        rotated_box.append([])
        for j in range(row):
            rotated_box[i].append(box[j][-i-1])
    print('rotate_box_counterclockwise_90')
    return rotated_box


def rotate_box_clockwise_90_with_falling_down(box: list[list[str]]) -> list[list[str]]:
    # rotate box clockwise 90 degrees
    row, col = len(box), len(box[0])
    rotated_box = []
    for i in range(col):
        rotated_box.append([])
        for j in range(row):
            rotated_box[i].append(box[-j-1][i])

    # things failing down
    m, n = len(rotated_box), len(rotated_box[0])
    for j in range(n):
        for i in range(-1, -m-1, -1):
            # find empty
            if rotated_box[i][j] != '.':
                continue
            empty_index = i
            thing_index = i - 1
            # find thing
            while -m-1 < thing_index <= -1:
                if rotated_box[thing_index][j] == '#':
                    rotated_box[empty_index][j], rotated_box[thing_index][j] = rotated_box[thing_index][j], rotated_box[empty_index][j]
                    break
                elif rotated_box[thing_index][j] == '*':
                    break
                else:
                    thing_index -= 1


    print('rotate_box_clockwise_90, then failing down')
    return rotated_box


def rotate_box_clockwise_90_with_falling_down3(box: list[list[str]]) -> list[list[str]]:
    # rotate box clockwise 90 degrees
    row, col = len(box), len(box[0])
    rotated_box = [['.']*row for _ in range(col)]
    for i in range(col):
        for j in range(row):
            rotated_box[i][j] = box[-j-1][i]

    # things failing down
    m, n = len(rotated_box), len(rotated_box[0])
    for j in range(n):
        for i in range(-1, -m-1, -1):
            # find empty
            if rotated_box[i][j] != '.':
                continue
            empty_index = i
            thing_index = i - 1
            # find thing
            while -m-1 < thing_index <= -1:
                if rotated_box[thing_index][j] == '#':
                    rotated_box[empty_index][j], rotated_box[thing_index][j] = rotated_box[thing_index][j], rotated_box[empty_index][j]
                    break
                elif rotated_box[thing_index][j] == '*':
                    # 如果遇到障碍,则不需要继续向上找thing了，因为无法fall下来
                    break
                else:
                    thing_index -= 1


    print('rotate_box_clockwise_90, then failing down')
    return rotated_box


def rotate_box_clockwise_90_with_falling_down2(box: list[list[str]]) -> list[list[str]]:
    row, col = len(box), len(box[0])

    # push all things to the right most
    for i in range(row):
        for j in range(-1, -col-1, -1):
            if box[i][j] != ".":
                continue
            empty = j
            thing = j - 1
            while -col - 1 < thing <= -1:
                if box[i][thing] == '#':
                    box[i][empty], box[i][thing] = box[i][thing], box[i][empty]
                    break
                elif box[i][thing] == '*':
                    break
                else:
                    thing -= 1

    # rotate box clockwise 90 degrees
    rotated_box = []
    for i in range(col):
        rotated_box.append([])
        for j in range(row):
            rotated_box[i].append(box[-j-1][i])


    print('push things to right most, then rotate_box_clockwise_90')
    return rotated_box


grid_box = [["#","#",".",".","*","."],
            ["#","#","#","*",".","."],
            ["#","#","#",".","#","."]]


def print_box(box):
    for row in box:
        print(row)

print_box(grid_box)
print('-' * 50)
print_box(rotate_box_clockwise_90(grid_box))
# print('-' * 50)
# print_box(rotate_box_clockwise_180(grid_box))
# print('-' * 50)
# print_box(rotate_box_counterclockwise_90(grid_box))
# print('-' * 50)
# print_box(rotate_box_clockwise_90_with_falling_down(grid_box))
print('-' * 50)
print_box(rotate_box_clockwise_90_with_falling_down3(grid_box))
