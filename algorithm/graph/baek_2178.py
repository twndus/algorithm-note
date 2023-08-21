# 백준: 미로 탐색 https://www.acmicpc.net/problem/2178
from collections import deque
n, m = list(map(int, input().split(' ')))
maze = []
for _ in range(n):
    maze.append(list(map(int, list(input()))))

queue = deque([(0, 0)])

maze[0][0] += 1
while queue:
    v = queue.popleft()
    value = maze[v[0]][v[1]]
    if v[0] == (n-1) and v[1] == (m-1):
        print(value-1)
        break
    for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx = v[0]+dx
        ny = v[1]+dy
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if maze[nx][ny] == 1:
            maze[nx][ny] = value + 1
            queue.append((nx,ny))
