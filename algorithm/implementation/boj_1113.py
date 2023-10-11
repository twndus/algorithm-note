# BOJ 1113 수영장 만들기
import sys
input = sys.stdin.readline
n,m = list(map(int,input().split()))
pool = [list(map(int, input().strip())) for _ in range(n)]

for row in pool:
    print(row)

# 둘러싸여진 곳을 찾는다: 사방으로 현재 위치보다 높은 값이 있는가? 모서리는 아닌가?
def outrange(r,c):
    return r<0 or c<0 or r>=n or c>=m

for r in range(n):
    for c in range(m):
        maxval = pool[r][c]
        out = False
        for dr,dc in zip((0,0,-1,1), (1,-1,0,0)):
            nr,nc = r+dr,c+dc
            if outrange(nr,nc):
                out = True
            else:
                maxval = max(maxval, pool[r][c])
        print(pool[r][c], maxval, out)
        if pool[r][c] < maxval and out:
            pool[r][c] = -1

for row in pool:
    print(row)
