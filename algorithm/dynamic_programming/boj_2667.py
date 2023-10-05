# BOJ 2667 단지번호붙이기: https://www.acmicpc.net/problem/2667
n = int(input())
maps = [list(map(int, list(input()))) for _ in range(n)]
result = []

def get_connected_items(r,c):
    stack = [(r,c)]
    maps[r][c] = -1
    result = 0 
    while stack:
        r,c = stack.pop()
        result += 1
        for dr,dc in zip((0,0,-1,1), (-1,1,0,0)):
            nr,nc = r+dr, c+dc
            if nr<0 or nr >= n or nc<0 or nc >= n: continue
            if maps[nr][nc] == 1:
                maps[nr][nc] = -1
                stack.append((nr,nc))
    return result


for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            result.append(get_connected_items(i, j))

print(len(result))
for i in sorted(result):
    print(i)
