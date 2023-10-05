n = int(input())
wine = [int(input()) for _ in range(n)]
d = [[0,0] for _ in range(n+1)]
d[1] = [wine[0], 0]

for i in range(2, n+1):
    # 연속이면 점프
    for j in range(i-1):
        d[i][0] = max(max(d[j]) + wine[i-1], d[i][0])
    # 연속이 아니면 이전 데이터에 i번째 더하기
    d[i][1] = d[i-1][0] + wine[i-1]

print(max(d[-1]+d[-2]))
