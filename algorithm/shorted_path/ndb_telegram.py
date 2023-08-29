# 이코테 최단경로 알고리즘 - 전보
import heapq

INF = 1e9
n, m, c = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = list(map(int, input().split()))
    graph[x].append([y, z])

def dikjstra(n, graph, c):

    h = []
    table = [INF for _ in range(n+1)]
    
    heapq.heappush(h, (0, c))

    while h:
        vc, vn = heapq.heappop(h)

        if table[vn] < vc:
            continue

        for nn, nc in graph[vn]:
            if vc+nc < table[nn]:
                table[nn] = min(vc+nc, table[nn])
                heapq.heappush(h, (vc+nc, nn))

    n_cities, max_time = 0, 0
    for t in table:
        if t != INF:
            n_cities += 1
            max_time = max(max_time, t)
    
    return n_cities, max_time

n_cities, max_time = dikjstra(n, graph, c)
print(n_cities, max_time)
