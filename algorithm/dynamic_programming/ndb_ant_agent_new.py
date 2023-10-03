# input
n = int(input())
storage = list(map(int, input().split()))

# bottom-up approach
d = [0]*n
d[0] = storage[0]
d[1] = storage[1]

for i in range(2, n):
    d[i] = max(d[i-2]+storage[i], d[i-1])

print(d[n-1])
