# 플로이드 워셜 알고리즘: 전체 노드 간 최단 경로 찾기
import sys
input = sys.stdin.readline

n, e = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for _ in range(e):
    n1, n2, cost = list(map(int, input().split()))
    graph[n1-1].append((n2-1, cost))

INF = 1e+9

def floyd_warshall(n, graph):
    maps = [[INF for _ in range(n)] for _ in range(n)]

    # 초기화
    for i in range(n):
        maps[i][i] = 0
        for gn, gc in graph[i]:
            maps[i][gn] = gc

    # 탐색
    for k in range(n):
        for a in range(n):
            for b in range(n):
                
                # 출발/끝 노드가 같거나, 매개노드와 같으면 통과
                if (a == b) or (a == k) or (b == k): continue

                # a -> k
                maps[a][b] = min(maps[a][b], maps[a][k] + maps[k][b])
    
    return maps


print(floyd_warshall(n, graph))
