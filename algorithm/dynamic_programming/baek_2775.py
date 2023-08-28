# 백준 DP: 부녀회장이 될테야 https://www.acmicpc.net/problem/2775

t = int(input())

data = []
for _ in range(t):
    k = int(input())
    n = int(input())
    data.append((k,n))

def dp_bottomup(k, n):
    d = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(1, n+1):
        d[0][i] = i

    for i in range(1, k+1):
        for j in range(1 ,n+1): 
            d[i][j] = d[i][j-1] + d[i-1][j]

    print(d[-1][-1])

for k,n in data:
    dp_bottomup(k, n)
