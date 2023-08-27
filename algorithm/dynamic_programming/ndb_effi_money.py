n, m = list(map(int, input().split()))
money = sorted([int(input()) for i in range(n)])
d = [0]*(m+1)

for i in range(1, m+1):
    options = []
    for m in money:
        if m>i:
            break
        elif d[i-m] >= 0:
            options.append(d[i-m]+1)

    print(i, options)
    if options:
        d[i] = min(options)
    else:
        d[i] = -1

print(d[-1])
