# BOJ 10810 공 넣기
n,m = list(map(int, input().split()))
baskets = [0]*n
for _ in range(m):
    i,j,k = list(map(int, input().split()))
    for idx in range(i-1, j):
        baskets[idx] = k

for i in range(n):
    print(baskets[i], end=' ')
