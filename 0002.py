# 2018/05/23

import math

l = int(input())
n = int(input())
x = [int(x) for x in input().split(',')]

min_time = max([min(_x, l-_x) for _x in x])

max_time = max([max(i,l-i) for i in x])

print('max_time = {}'.format(max_time))
print('min_time = {}'.format(min_time))
