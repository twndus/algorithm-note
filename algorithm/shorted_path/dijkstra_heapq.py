# 다익스트라 with 우선순위 큐
import sys, heapq

input = sys.stdin.readline # 여러 줄 입력받기 위해
n, e = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
INF = 1e+9

for _ in range(e):
    n1, n2, cost = list(map(int,input().split()))
    graph[n1].append([n2, cost])

def dijkstra_algorithm(n, graph, start):
    
    table = [INF for _ in range(n+1)]
    table[start] = 0

    h = []
    heapq.heappush(h, (0, start))

    while h:

        # 최단경로 노드 찾기
        vc, v = heapq.heappop(h)
        print(v, vc)

        # 방문한 (이미 최단경로에 도달한) 노드 패스
        if table[v] < vc:
            continue
       
        for nn, nc in graph[v]:
            
            # 방문여부 상관없이 최단경로면 업데이트
            if nc+vc < table[nn]:
                print(nn, nc+vc, table[nn])
                table[nn] = nc+vc
                heapq.heappush(h, (nc+vc, nn))

    print(table[1:])
        
print()
dijkstra_algorithm(n, graph, 1)
    
