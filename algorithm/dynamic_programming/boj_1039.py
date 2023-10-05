# BOJ 1039 교환 https://www.acmicpc.net/problem/1039
from collections import deque
import math
n, k = list(map(int, input().split()))
n = list(map(int, list(str(n))))
d = set()

# 최댓값 위치 > 최솟값 위치인 경우 두 위치를 바꿈
# 그렇지 않을 때는 그 다음 최댓값과 최솟값, 최댓값과 그 다음 최솟값읠 위치를 바꾸고
# 이 과정이 k번에 도달하면 멈추고, 그 이하인데 두 값이 같아지면 -1

def get_index(n, maxval, minval):
    maxi = n.index(maxval)
    mini = n.index(minval)
    return maxi, mini

def bfs(n, maxval, minval):
    global k,d
    queue = deque([[n, 0]])
    while queue:
        n, t = queue.popleft()

        if t >= k:
            d.add(int(''.join(map(str,n)))) 
            continue
        
        for i in range(len(n)-1):
            for j in range(i, len(n)):
                if n[j] == 0: continue
                n_copy = n.copy()
                n[i], n[j] = n[j], n[i]
                if int(''.join(map(str,n))) in d: continue
                queue.append([n, i+1])
        print(d, queue)

num_of_zero = sum([1 if i == 0 else 0 for i in n])

if math.factorial(len(n))-num_of_zero-1 < k:
    print(-1)
    exit()

bfs(n, max(n), min(n))
if len(d)<1:
    print(-1)
if len(d) == 1 and d=={-1}:
    print(-1)
else:
    print(min(d))


#def get_index(n, maxval, minval):
#    maxi = n.index(maxval)
#    mini = n.index(minval)
#    return maxi, mini
#
#def bfs(n, maxval, minval):
#    global k,d
#    i = 0
#    queue = deque([[n, maxval, minval, i]])
#    while queue:
#        n, maxval, minval, i = queue.popleft()
#        
#        if minval == 0 and i<k:
#            continue
#        if maxval == minval and i<k:
#            d.add(int(''.join(map(str,n)))) 
#            continue
#
#        if maxval != minval and i>=k:
#            d.add(int(''.join(map(str,n)))) 
#            continue 
#
#        maxi, mini = get_index(n,maxval,minval)
#
#        if minval != 0 and maxi > mini:
#            n[maxi], n[mini] = n[mini], n[maxi]
#
#        n_copy = n.copy()
#        n_copy[mini] = -1
#        queue.append([n, max(n_copy), minval, i+1])
#
#        n_copy = n.copy()
#        n_copy[maxi] = 1e6+1
#        queue.append([n, maxval, min(n_copy), i+1])
#
#        print(d, queue)

#def dfs(n, maxval, minval, i):
#    if maxval == minval and i<k:
#        d.add(-1)
#    if i >= k:
#        d.add(int(''.join(n))) 
#
#    maxi = n.index(maxval)
#    mini = n.index(minval)
#
#    if maxi > mini:
#        n[maxi], n[mini] = n[mini], n[maxi]
#        dfs(n, maxval, minval, i+1)
#    else:
#        n_copy = n.copy()
#        n_copy.maxi = -1
#        dfs(n, max(n_copy), minval, i+1)
#        n_copy = n.copy()
#        n_copy.mini = 1e6+1
#        dfs(n, maxval, min(n_copy), i+1)        
#
#num_of_zero = sum([1 if i == 0 else 0 for i in n])
#
#if math.factorial(len(n))-num_of_zero-1 < k:
#    print(-1)
#    exit()
#
#bfs(n, max(n), min(n))
#if len(d)<1:
#    print(-1)
#if len(d) == 1 and d=={-1}:
#    print(-1)
#else:
#    print(min(d))
