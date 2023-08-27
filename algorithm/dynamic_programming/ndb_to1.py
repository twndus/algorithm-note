# 이코테: 1로 만들기
n = int(input())
d = [0]*(n+1)

d[1] = 0

for i in range(2, n+1):
    options = []
    if not i%5:
        options.append(d[i//5])
    if not i%3:
        options.append(d[i//3])
    if not i%2:
        options.append(d[i//2])
    options.append(d[i-1])

    d[i] += min(options) + 1
    print(i, options)

print(d[-1])


