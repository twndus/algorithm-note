# 이코테 최단 경로 알고리즘: 미래 도시 문제
## 플로이드 워셜 알고리즘 활용
import sys
input = sys.stdin.readline
INF = 1e9

n,m = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    n1, n2 = list(map(int, input().split()))
    graph[n1].append(n2)
    graph[n2].append(n1)
x,k = list(map(int, input().split()))

def floyd_warshall(n, graph, start, k, end):

    table = [[INF for _ in range(n+1)] for _ in range(n+1)]

    for v in range(1, n+1):
        for gv in graph[v]:
            table[v][gv] = 1
            table[gv][v] = 1

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                table[a][b] = min(table[a][b], table[a][k]+table[k][b])

    a_k_x = table[start][k] + table[k][end]
    if a_k_x < 1e9:
        return a_k_x
    else:
        return -1

print(floyd_warshall(n, graph, 1, k, x))
