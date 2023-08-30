# 백준: 1로 만들기 https://www.acmicpc.net/problem/1463
import sys
sys.setrecursionlimit(10**6)

n = int(input())
answer = 0

d = [-1 for _ in range(10**6+1)]
d[1], d[2], d[3] = 0, 1, 1

# bottom-up
for i in range(4, n+1):
    d[i] = 1+d[i-1]
    if i%3 == 0:
        d[i] = min(d[i], 1+d[i//3])
    if i%2 == 0:
        d[i] = min(d[i], 1+d[i//2])

print(d[n])
