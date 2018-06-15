'''
大きさがN*Mの庭があります。そこに雨が振り、水たまりができました。水たまりは8近傍で隣接している場合につながっているとみなします。全部でいくつの水たまりがあるでしょうか？
'''

n = 10
m = 12
rain = [[1,0,0,0,0,1,0,0,0,1,1,0],
        [0,1,1,1,0,0,0,0,0,1,1,1],
        [0,0,0,0,1,1,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,0,0,1,0,0],
        [0,1,0,1,0,0,0,0,0,1,1,0],
        [1,0,1,0,1,0,0,0,0,0,1,0],
        [0,1,0,1,0,0,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,0,0,0,1,0]]

flags = [[0 for i in range(m)] for j in range(n)]

puddle = 0

def get_random_puddle():
    print('get position')
    position = []
    for i in range(n):
        for j in range(m):
            if rain[i][j] == 1 and flags[i][j] == 0:
                position = [i, j]
                break
    return position

def dfs(x, y):
    if x < 0 or x >= n:
        return 0

    if y < 0 or y >= m:
        return 0

    print("[{}, {}] {} ".format(x,y,rain[x][y]))


    if rain[x][y] == 1:
        flags[x][y] = 1

    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            else:
                if x+i <0 or x+i >= n:
                    continue
                elif y+j <0 or y+j >= m:
                    continue
                if rain[x+i][y+j] == 1 and flags[x+i][y+j] == 0:
                    dfs(x+i, y+j)
                    sum += 1

while True:
    position = get_random_puddle()
    if not position:
        break
    dfs(position[0], position[1])
    puddle += 1

print('puddle = ', puddle)
