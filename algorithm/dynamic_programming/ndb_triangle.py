# input
n = int(input())
triangle = [list(map(int,input().split())) for _ in range(n)]

for r in range(1, n):
    for c in range(len(triangle[r])):
        if c == 0:
            triangle[r][c] = triangle[r][c]+triangle[r-1][c]
        elif c == r:
            triangle[r][c] = triangle[r][c]+triangle[r-1][c-1]
        else:
            triangle[r][c] = triangle[r][c]+max(
                triangle[r-1][c], triangle[r-1][c-1])
print(max(triangle[n-1]))
