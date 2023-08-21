# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# DFS - recursive
def dfs2(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)

# DFS - stack
def dfs3(graph, stack, visited):
    while stack:
        node = stack.pop()
        if visited[node]: continue
        visited[node] = True
        print(node, end=' ')
        for i in graph[node][::-1]:
            if not visited[i]:
                stack.append(i)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
print("DFS 1: ")
visited = [False] * 9
dfs(graph, 1, visited)
print("\nDFS 2: ")
visited = [False] * 9
dfs2(graph, 1, visited)
print("\nDFS 3: ")
visited = [False] * 9
dfs3(graph, [1], visited)
