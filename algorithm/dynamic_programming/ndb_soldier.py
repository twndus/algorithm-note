# 이코테: 병사 배치하기
## 풀이 전략 - LIS 알고리즘

n = int(input())
soldiers = list(map(int, input().split()))[::-1]
d = [1]*n

for i in range(1, n):
    options = []
    for j in range(i):
        if soldiers[i] > soldiers[j]:
            d[i] = max(d[i], d[j]+1)
    print(soldiers, d)

print(n-d[-1])
