# BOJ 1715 카드 정렬하기
import heapq
n = int(input())

pq = []
for _ in range(n):
    heapq.heappush(pq, int(input()))

answer = 0
before = heapq.heappop(pq)
for num in range(1, n):
    now = heapq.heappop(pq)
    before += now
    answer += before
    heapq.heappush(pq, before)
    before = heapq.heappop(pq)
print(answer)

