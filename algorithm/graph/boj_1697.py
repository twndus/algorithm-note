# BOJ 1067 숨바꼭질
from collections import deque
n, k = list(map(int, input().split()))

queue = deque([(n,0)])
visited = set()

def dist(n,k):
    return max(n,k)-min(n,k)

while queue:
    nnow,tnow = queue.popleft()
    visited.add(nnow)

    if dist(n,k) <= tnow:
        tnow = dist(n,k)
        break
    if nnow == k:
        break

    if nnow+1 not in visited: queue.append((nnow+1, tnow+1))
    if nnow-1 not in visited: queue.append((nnow-1, tnow+1))
    if nnow*2 not in visited and dist(nnow*2,k) < dist(n,k): queue.append((nnow*2, tnow+1))

print(tnow)
