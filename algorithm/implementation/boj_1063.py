# BOJ 1073 킹
row = [8,7,6,5,4,3,2,1]
column = ['A','B','C','D','E','F','G','H']
k,s,n = input().split()
commands = [input() for _ in range(int(n))]
dirs = ['R','L','B','T','RT','LT','RB','LB']
dr,dc = (0,0,1,-1,-1,-1,1,1),(1,-1,0,0,1,-1,1,-1)

def get_coord(pos):
    return row[int(pos[1])-1]-1, column.index(pos[0])

def get_code(pos):
    return column[pos[1]]+str(row[pos[0]])

def outrange(r,c):
    return r<0 or r>=8 or c<0 or c>=8

kr,kc = get_coord(k)
sr,sc = get_coord(s)

for c in commands:
    d = dirs.index(c)
    nkr,nkc = kr+dr[d],kc+dc[d]
    nsr,nsc = sr+dr[d],sc+dc[d]
    
    if outrange(nkr,nkc): continue

    if nkr==sr and nkc==sc:
        if outrange(nsr, nsc): continue
        kr,kc = nkr,nkc
        sr,sc = nsr,nsc
    else:
        kr,kc = nkr,nkc

print(get_code((kr,kc)))
print(get_code((sr,sc)))
