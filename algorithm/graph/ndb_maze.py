# 이코테: 미로 찾기 https://www.youtube.com/watch?v=7C9RgOcvkvo&t=2879s
from collections import deque
def solution(n,m,maze):
    queue = deque([(0,0)])
    dirs = ((1,0), (-1,0), (0,1), (0,-1))

    while queue:
        v = queue.popleft()
        if (v[0] == n-1) and (v[1] == m-1):
            return maze[v[0]][v[1]]
        for dx,dy in dirs:
            nx,ny = v[0]+dx,v[1]+dy
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] += maze[v[0]][v[1]]
                queue.append((nx,ny))

if __name__ == '__main__':
    n,m = 5,6
    maze = [[1,0,1,0,1,0], [1,1,1,1,1,1], [0,0,0,0,0,1], [1,1,1,1,1,1], [1,1,1,1,1,1]]
    ans = 10
    print(solution(n,m,maze), ans)
