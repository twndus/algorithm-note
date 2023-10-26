# BOJ 1717 집합의 표현
import sys
input = sys.stdin.readline
n,m = list(map(int, input().split()))
result = []
for _ in range(m):
    c,a,b = list(map(int, input().split()))
    if c == 0:
        ?? = set(a)+set(b)
        pass
    else:
        answer = 'NO'
        result.append(answer)
    
