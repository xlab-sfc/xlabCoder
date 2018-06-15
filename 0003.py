'''
n 個の正の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] と正の整数 a が与えられる。これらの整数から何個かの整数を選んで総和が k になるようにすることが可能か判定せよ。可能ならば "YES" と出力し、不可能ならば "NO" と出力せよ。
'''
# n = int(input())
# a = [int(x) for x in input().split(',')]
# k = int(input())
n = 4
a = [1,2,4,7]
k = 13

def dfs(i, sum):
    if i == n:
        return sum == k

    if dfs(i+1, sum + a[i]):
        return True

    if dfs(i+1, sum):
        return True

    return False

print(dfs(0,0))
