# 백준: 2xn 타일링2 https://www.acmicpc.net/problem/11727

n = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 3 #(1x2 *2, 2x1 *2)

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]*2

print(d[n]%10007)
