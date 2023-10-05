# 백준 - 계단오르기 https://www.acmicpc.net/problem/2579
n = int(input())
stairs = [int(input()) for _ in range(n)]

d = [[0 for _ in range(2)] for _ in range(n+1)] # 0,1
d[1] = [stairs[0],-1]

for i in range(2,n+1):
    #0: 점프 전 메모리 중 큰 값
    d[i][0] = max(d[i-2][0], d[i-2][1])+stairs[i-1]
    #1: 1연속 직전 계단
    d[i][1] = d[i-1][0]+stairs[i-1]

print(max(d[-1]))
