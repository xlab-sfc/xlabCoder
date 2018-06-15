'''
大きさがN*Mの庭があります。そこに雨が振り、水たまりができました。水たまりは8近傍で隣接している場合につながっているとみなします。全部でいくつの水たまりがあるでしょうか？
'''

def debug_print(field):
    for xx in field:
        for yy in xx:
            print(yy, end="")
        print("\n")

def lake_counting(field):

    debug_print(field)

    field_x_length = len(field)
    field_y_length = len(field[0])

    lake_count = 0

    def dfs(x, y):
        field[x][y] = '.'
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx = x + dx
                ny = y + dy
                if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and field[nx][ny] == 'W'):
                    dfs(nx, ny)

    for i in range(0, field_x_length):
        for j in range(0, field_y_length):
            if (field[i][j] == 'W'):
                dfs(i, j)
                lake_count += 1

    return lake_count

field = [
    ['W', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['.', 'W', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', 'W'],
    ['.', '.', '.', '.', 'W', 'W', '.', '.', '.', 'W', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['W', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.'],
]

print(lake_counting(field))
