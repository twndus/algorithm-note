# BOJ 7579 앱
n,m = list(map(int,input().split()))
memories = list(map(int,input().split()))
costs = list(map(int,input().split()))

maxmem, maxcost = sum(memories), sum(costs)
dp = [[maxcost for _ in range(maxmem-m+1)] for _ in range(n+1)]

def search(i, mem):
    if i<1: return 0
    if dp[i-1][mem] == maxcost:
        search(i-1, mem)
        dp[i][mem] = min(dp[i][mem], dp[i-1][mem])
    if mem-memories[i-1] >= 0:
        if dp[i-1][mem-memories[i-1]] == maxcost:
            search(i-1, mem-memories[i-1])
        dp[i][mem] = min(dp[i][mem], dp[i-1][mem-memories[i-1]]-costs[i-1])
    return dp[i][mem]

print(search(n,maxmem-m))


# m 이상이 되어야 하며, 비용이 최소가 되어야 함
# 우선 모두 포함. costs 최대
# 하나씩 빼거나 그냥 두거나. 뺄 때는 빼도 m 이상이어야 함.
