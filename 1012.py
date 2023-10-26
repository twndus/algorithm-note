import sys

input = sys.stdin.readline
t = int(input())

def mark_connected(maps,r,c,n,m):

    stack = [(r,c)]
    while stack:
        r,c = stack.pop()
        for dr,dc in zip((0,0,-1,1),(1,-1,0,0)):
            nr,nc = r+dr, c+dc
            print(nr,nc,maps[nr][nc],maps[1][1])
            if nr<0 or nr>=n or nc<0 or nc>=m: break
            if maps[nr][nc] == 1:
                maps[nr][nc] = 0
                stack.append((nr,nc))
        print(stack)
    return maps

def get_element_num(maps,m,n):
    num_elements = 0
    
    for r in range(n):
        for c in range(m):
            if maps[r][c] == 1:
                maps[r][c] = 0
                maps = mark_connected(maps,r,c,n,m)
                num_elements += 1
                print(maps)
                print()

    return num_elements


for _ in range(t):

    m,n,k = list(map(int,input().split()))
    maps = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        c,r = list(map(int,input().split()))
        maps[r][c] = 1

    print(maps)
    print(get_element_num(maps,m,n))
    exit()
