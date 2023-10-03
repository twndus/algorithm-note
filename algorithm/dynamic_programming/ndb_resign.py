# input
n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

# bottom-up approach
d = [0] * 21 # 5+15+1 = 21 (n+1)
for i in range(n):
    if schedule[i][0] == 1:
        # 오늘로 끝나는 일이면, 이전까지 최댓값에 오늘 금액을 더함
        if i>0:
            d[i] = max(d[i], d[i-1]+schedule[i][1])
        else:
            d[i] = schedule[i][1]

    else:
        # 오늘은 이전까지의 최댓값으로 업데이트
        if i>0: d[i] = max(d[i-1], d[i])
        # 미래 끝날 시점에 최댓값을 업데이트
        future = i+schedule[i][0]-1
        d[future] = max(d[future], d[i-1]+schedule[i][1])

print(d[n-1])
