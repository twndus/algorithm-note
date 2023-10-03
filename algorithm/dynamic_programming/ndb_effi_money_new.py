# input
n,m = list(map(int, input().split()))
coins = [int(input()) for _ in range(n)]

# bottom-up approach
d = [-1]*(m+1)

for coin in coins:
    if coin >= m+1: continue
    d[coin] = 1

for i in range(1, m+1):
    options = []
    for coin in coins:
        if i-coin == 0:
            options.append(1)
        elif i-coin > 1 and d[i-coin] != -1:
            options.append(d[i-coin]+1)
    if len(options):
        d[i] = min(options)

print(d[m])
