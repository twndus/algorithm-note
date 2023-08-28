# 백준 DP: RGB거리 https://www.acmicpc.net/problem/1149

n = int(input())

houses = []
for _ in range(n):
    houses.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(3):
        houses[i][j] += min(houses[i-1][(j-1)%3], houses[i-1][(j+1)%3])

print(min(houses[-1]))
