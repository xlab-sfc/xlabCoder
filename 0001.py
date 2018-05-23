# 2018/05/23

# 任意の数の数字が与えられた時に、
# そのうちの3つの数字を辺の長さとする三角形の中で、
# 最大の周長はいくつ？

# n : 与えられる数字の数
# ( n = 4 )
# a : 与えられる任意の数字の入った配列
# ( a = {2, 3, 5, 9} )

n = input()

a = [ int(x) for x in input().split(',')]

max_len = 0

for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if a[k] < a[i]+a[j]:
                max = a[k] + a[i] + a[j]
                if max_len < max:
                    max_len = max

print(max_len)
