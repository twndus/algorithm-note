# 문제: DFS와 BFS https://www.acmicpc.net/problem/1260
from collections import deque
import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

def dfs(graph, stack, visited):
    v = stack.pop()
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            stack.append(i)
            dfs(graph, stack, visited)

def bfs(graph, queue, visited):
    if not queue:
        return
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)
    bfs(graph, queue, visited)

def solution():
    n,m,v = list(map(int, input().split()))
    graph = {i+1:[] for i in range(n)}
    for _ in range(m):
        k,v_ = list(map(int, input().split()))
        graph[k].append(v_)
        graph[v_].append(k)

    for k in graph.keys():
        graph[k] = sorted(list(set(graph[k])))

    stack = [v]
    visited = [False]*(n+1)
    visited[v] = True
    dfs(graph, stack, visited)

    print()
    queue = deque([v])
    visited = [False]*(n+1)
    visited[v] = True
    bfs(graph, queue, visited)


if __name__ == '__main__':
    solution()
