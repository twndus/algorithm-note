# 이코테 최단 경로 알고리즘: 미래 도시 문제
import sys, heapq
input = sys.stdin.readline
INF = 1e9

n,m = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    n1, n2 = list(map(int, input().split()))
    graph[n1].append(n2)
    graph[n2].append(n1)
x,k = list(map(int, input().split()))

def dijstra(n, graph, start, end):

    h = []
    table = [INF for _ in range(n+1)]
    heapq.heappush(h, (0, start))

    while h:
        vc, vn = heapq.heappop(h)
        if table[vn] < vc:
            continue
        for cn in graph[vn]:
            table[cn] = min(table[cn], vc+1)
            heapq.heappush(h, (vc+1, cn))

    return table[end]

a_to_k = dijstra(n, graph, 1, k)
k_to_y = dijstra(n, graph, k, x)

if (a_to_k != INF) and (k_to_y != INF):
    print(a_to_k+k_to_y)
else:
    print(-1)
            
