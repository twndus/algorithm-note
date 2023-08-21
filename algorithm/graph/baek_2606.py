# 문제: 바이러스 https://www.acmicpc.net/problem/2606

n_computers = int(input())
n_edges = int(input())

graph = {k:[] for k in range(1, n_computers+1)}

for _ in range(n_edges):
    n1, n2 = list(map(int, input().split(' ')))
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [0] * (n_computers+1)
visited[1] = 1

def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

dfs(1)
print(sum(visited)-1)
