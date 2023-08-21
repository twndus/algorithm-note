# 문제: 음료수 얼려먹기
n, m = list(map(int, input().split(' ')))

frame = []
for _ in range(n):
    frame.append(input())

def dfs(frame, node, visited):
    i, j = node

    if i<0 or i>=n or j<0 or j>=m:
        return
    else:
        if not visited[i][j] and (frame[i][j] == '0'):
            visited[i][j] = 1
            dfs(frame, (i+1, j), visited)
            dfs(frame, (i-1, j), visited)
            dfs(frame, (i, j+1), visited)
            dfs(frame, (i, j-1), visited)

visited = [[0 for _ in range(m)] for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if (not visited[i][j]) and (frame[i][j] == '0'):
            dfs(frame, (i, j), visited)
            answer += 1

print(answer)
