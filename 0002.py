# 2018/05/23

# 問題 : http://poj.org/problem?id=1852

'''
長さLcmの棒があり、その上に蟻がn匹いて、その蟻たちは端からx0, x1, x2...xncmの場所にいます。蟻たちは初め左右のどちらを向いているかはわからず、1cm/secの速さで棒の上を移動します。蟻たちはぶつかるともと来た方向に戻ります。蟻たちが棒のはじまでくると蟻たちは棒から落ちます。

全ての蟻たちが落ちるまでにかかる時間を求めなさい。（秒）

制約: 1 <= L <= 10^6, 1 <= n <= 10^6, 0 <= xi <= L

''' 


import math

l = int(input())
n = int(input())
x = [int(x) for x in input().split(',')]

min_time = max([min(_x, l-_x) for _x in x])

max_time = max([max(i,l-i) for i in x])

print('max_time = {}'.format(max_time))
print('min_time = {}'.format(min_time))
