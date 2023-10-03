def max_gold(n,m,maps):
    for c in range(1, m):
        for r in range(n):
            if r == 0:
                maps[r][c] = maps[r][c] + max(maps[r][c-1], maps[r+1][c-1])
            elif r == n-1:
                maps[r][c] = maps[r][c] + max(maps[r][c-1], maps[r-1][c-1])
            else:
                maps[r][c] = maps[r][c] + max(
                    maps[r-1][c-1], maps[r][c-1], maps[r+1][c-1])

    maxval = 0
    for i in range(n):
        maxval = max(maxval, maps[i][-1])

    return maxval

# input
t = int(input())
results = []
for _ in range(t):
    n,m = list(map(int,input().split()))
    data = list(map(int,input().split()))
    maps = [data[i*m:(i+1)*m] for i in range(n)]
    results.append(max_gold(n,m,maps))

for i in range(t):
    print(results[i])
