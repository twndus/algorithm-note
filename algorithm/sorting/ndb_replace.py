n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

answer = 0
for i in range(k):
    answer += b[i]

for i in range(k, n):
    answer += a[i]

print(answer)

