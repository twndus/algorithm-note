# 입력 받기
n = int(input())
maps = []
for _ in range(n):
    maps.append(list(input()))
k = int(input())-1

dr,dc = [1,0,-1,0],[0,-1,0,1] # 하좌상우
direction = k//n
slash_dict = {0:1, 1:0, 2:3, 3:2}
slash_op_dict = {0:3, 1:2, 2:1, 3:0}

if direction==0:
    r,c = 0, k%n
elif direction==1:
    r,c = k%n, n-1
elif direction==2:
    r,c = n-1, n-1-k%n
else:
    r,c = n-1-k%n, 0

counter = 0
while r>=0 and r<n and c>=0 and c<n:
    if maps[r][c] == '/':
        direction = slash_dict[direction]
    else:
        direction = slash_op_dict[direction]
    r,c = r+dr[direction], c+dc[direction]
    counter += 1

print(counter)
