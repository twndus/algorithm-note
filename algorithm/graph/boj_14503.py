# BOJ 14503 로봇청소기
n,m = list(map(int, input().split()))
r,c,d = list(map(int, input().split()))
room = [list(map(int, input().split())) for _ in range(n)]
dr,dc = (-1, 0, 1, 0), (0, 1, 0, -1)
result = 0

while True:

    if room[r][c] == 0:
        room[r][c] = 2
        result += 1

    for i in range(1, 5):
        nd = (d-i+4)%4
        nr, nc = r+dr[nd], c+dc[nd]
        if nr<0 or nr>=n or nc<0 or nc>=m: continue
        if room[nr][nc] == 0:
            r,c,d = nr,nc,nd
            break
    else:
        nr, nc = r-dr[d], c-dc[d]
        if nr<0 or nr>=n or nc<0 or nc>=m: break 
        if room[nr][nc] == 1: break
        r,c,d = nr,nc,d

print(result)
