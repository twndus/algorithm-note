# BOJ 1946 신입사원
import heapq
t = int(input())
results = []
for _ in range(t):

    n = int(input())

    candies = []
    for _ in range(n):
        r,c = list(map(int,input().split()))
        heapq.heappush(candies, (-r,c))
    
    #init
    r,c = heapq.heappop(candies)
    maxc = c
    result = 1
    
    for i in range(n-1):
        r,c = heapq.heappop(candies)
        if maxc > c:
            result += 1

#
#
#    result = 1
#
#    for _ in range(n-1):
#        r,c = heapq.heappop(candies)
#        if minc < c:
#        s1,s2 = candies[i]
#
#        if s2<min1[1]:
#            continue
#        elif s1<min2[0]:
#            continue
#
#        if s1<min1[0]:
#            min1 = s1,s2
#        if s2<min2[1]:
#            min2 = s1,s2
#        result += 1
#
##        if s2>pq1[0][1] or s1>pq2[0][1]:
##            heapq.heappush(pq1,[s1,s2])
##            heapq.heappush(pq2,[s2,s1])
##            result += 1
#
    results.append(result)

for result in results:
    print(result)
