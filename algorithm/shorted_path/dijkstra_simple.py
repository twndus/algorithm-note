# 다익스트라 단순
import sys

input = sys.stdin.readline # 여러 줄 입력받기 위해
n, e = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
INF = 1e+9

for _ in range(e):
    n1, n2, cost = list(map(int,input().split()))
    graph[n1].append([n2, cost])

def get_closest_node(table, visited):
    min_val = INF
    node = -1
    for i, t in enumerate(table[1:]):
        if (min_val > t) and (not visited[i+1]):
            min_val = t
            node = i+1
    return node, min_val

def dijkstra_algorithm(n, graph, start):
    
    # 최단 경로 저장 테이블
    table = [INF for _ in range(n+1)]
    # 방문 확인 테이블
    visited = [0 for _ in range(n+1)]
    # 시작노드의 거리 0
    table[start] = 0

    while sum(visited) < len(visited)-1:
        
        # 최단경로 노트 찾기
        v, vc = get_closest_node(table, visited)
        visited[v] = 1
        print(v, vc)
       
        for nn, nc in graph[v]:

            # 방문한 경우는 통과
            if visited[nn]: continue

            # 방문안한 노드에 대해서
            if nc+vc < table[nn]:
                print(nn, nc+vc, table[nn])
                table[nn] = nc+vc
    
    print(table[1:])

print()        
dijkstra_algorithm(n, graph, 1)
    
