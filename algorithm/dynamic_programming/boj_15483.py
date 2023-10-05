# 백준 - 최소 편집 https://www.acmicpc.net/problem/15483
a = input()
b = input()

n,m = len(a), len(b)

# dp table 생성 및 초기화
dp = [[0 for i in range(m+1)] for j in range(n+1)]
dp[0] = [i for i in range(m+1)]
for j in range(n+1):
    dp[j][0] = j

# dp table 확인
for row in dp:
    print(dp)

for i in range(1,n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])
