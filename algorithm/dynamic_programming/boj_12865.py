# BOJ 12865 평범한 배낭: knapsack algorithm
n,k = list(map(int,input().split()))
weights, values = [], []
for _ in range(n):
    w,v = list(map(int,input().split()))
    weights.append(w)
    values.append(v)

dp = [[0 for i in range(k+1)] for _ in range(n+1)]

def search(i,w):
    if i<1: return 0
    if dp[i-1][w]==0:
        search(i-1, w)
    dp[i][w] = max(dp[i][w], dp[i-1][w])
    if w-weights[i-1]>=0:
        if dp[i-1][w-weights[i-1]]==0:
            value = search(i-1, w-weights[i-1])
        dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]]+values[i-1])
    return dp[i][w]
print(search(n,k))
