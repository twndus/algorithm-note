# 문제: 연결 요소의 개수 https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m = list(map(int, input().split(' ')))
graph = {k:[] for k in range(1, n+1)}
for _ in range(m):
    n1, n2 = list(map(int, input().split(' ')))
    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
    
visited = [False] * (n+1)
answer = 0

for node in range(1, n+1):
    if not visited[node]:
        dfs(node)
        answer += 1
print(answer)
