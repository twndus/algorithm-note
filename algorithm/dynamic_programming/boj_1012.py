# BOJ 1012 유기농 배추 https://www.acmicpc.net/problem/1012
from collections import deque
t = int(input())

# bfs
def get_connected_items(r,c, n,m, maps):
    queue = deque([[r,c]])
    maps[r][c] = -1
    while queue:
        r,c = queue.popleft()
        for dr,dc in zip((0,0,1,-1), (1,-1,0,0)):
            nr,nc = r+dr, c+dc
            if nr<0 or nr>=n or nc<0 or nc>=m: continue
            if maps[nr][nc] == 1:
                maps[nr][nc] = -1
                queue.append((nr,nc))

# dfs
def _get_connected_items(r,c, n,m, maps):
    stack = [[r,c]]
    maps[r][c] = -1
    while stack:
        r,c = stack.pop()
        for dr,dc in zip((0,0,1,-1), (1,-1,0,0)):
            nr,nc = r+dr, c+dc
            if nr<0 or nr>=n or nc<0 or nc>=m: continue
            if maps[nr][nc] == 1:
                maps[nr][nc] = -1
                stack.append((nr,nc))

def test():
    m,n,k = list(map(int,input().split()))
    maps = [[0 for j in range(m)] for i in range(n)]
    for _ in range(k):
        x,y = list(map(int,input().split()))
        maps[y][x] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                get_connected_items(i,j,n,m,maps)
                result += 1
    return result

results = []
for _ in range(t):
    results.append(test())

for result in results:
    print(result)
