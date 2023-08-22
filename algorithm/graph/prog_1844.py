# 프로그래머스: 게임 맵 최단거리 https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3
from collections import deque

def solution(maps):
    start = (0,0)
    dirs = ((1,0), (-1,0), (0,1), (0,-1))
    n,m = len(maps), len(maps[0])
    queue = deque([start])

    maps[0][0] = 1
    while queue:
        v = queue.popleft()
        if v == (n-1,m-1):
            return maps[v[0]][v[1]]
        for dx,dy in dirs:
            nx,ny = v[0]+dx, v[1]+dy
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if maps[nx][ny]==1:
                maps[nx][ny] += maps[v[0]][v[1]]
                queue.append((nx,ny))

    return -1


if __name__ == '__main__':
    ex1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    ans1 = 11
    print(solution(ex1), ans1)

    ex2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
    ans2 = -1
    print(solution(ex2), ans2)

