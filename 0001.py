# 2018/05/23

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
