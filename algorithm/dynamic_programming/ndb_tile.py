# input
n = int(input())

# bottom-up approach
d = [0] * (n+1)
d[1] = 1
d[2] = 3 #(1x2 *2, 2x1 *2, 2x2 *1)

for i in range(3, n):
    d[i] = d[i-1] + d[i-2]*2

print(d[n-1])
