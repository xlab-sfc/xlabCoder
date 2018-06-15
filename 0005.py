from collections import deque

n = 10
m = 10

field = [
    ['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
    ['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['#', '#', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#'],
]

que =  deque()

len = 0

start = [0, 1]

que.append(start)

iter = 0
bFinish = False

while True:
    iter += 1

    def search_around(x, y):
        global bFinish;
        print('search : {} {}'.format(x, y))
        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) == 1 and abs(j) == 1:
                    continue
                elif x+i <0 or x+i >= n:
                    continue
                elif y+j <0 or y+j >= m:
                    continue
                elif field[x+i][y+j] == '.':
                        _pos = [x+i, y+j]
                        que.append(_pos)
                        field[x+i][y+j] = '#'
                        print('{} {} appended to que'.format(x+i, y+j))
                elif field[x+i][y+j] == 'G':
                    bFinish = True
                    print('{} {} = GOAL!'.format(x+i, y+j))
                    break
            else:
                continue
            break

    print('iter : ', iter)
    for _ in list(que):
        pos = que.popleft()
        search_around(pos[0], pos[1])

    if bFinish:
        print('iter : ', iter)
        break
