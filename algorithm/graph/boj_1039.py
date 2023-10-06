# BOJ 1039 포기..
from collections import deque
n,k = list(map(int, input().split()))
n = list(map(int, str(n)))

zero_count = sum([1 if e == 0 else 0 for e in n])
if (len(n) == 2 and zero_count == 1) or len(n)==1:
    print(-1)
    exit()
if len(n)-zero_count < 2:
    print(int(''.join(list(map(str, n)))))
    exit()
if len(n)-zero_count < zero_count:
    print(int(''.join(list(map(str, sorted(n, reverse=True))))))
    exit()
    
result = set()
queue = deque([(n, 0)])

while queue:
    nnew, count = queue.popleft()
    if count>= k:
        result.add(int(''.join(list(map(str, nnew)))))
        continue
    else:
        for i in range(len(n)-1):
            for j in range(i+1, len(n)):
                if i==0 and nnew[j] == 0: continue
                n_copy = nnew.copy()
                n_copy[i], n_copy[j] = n_copy[j], n_copy[i]
                queue.append((n_copy, count+1))

if len(result) < 1:
    print(-1)
else:
    print(max(result))
