# input
n = int(input())
soldiers = list(map(int,input().split()))

d = [1]*n

for i in range(1, n):
    # i 이전까지의 위치를 모두 확인
    for j in range(i):
        if soldiers[j] > soldiers[i]: # 조건을 만족하면
            d[i] = max(d[i], d[j]+1)

print(n-max(d))
