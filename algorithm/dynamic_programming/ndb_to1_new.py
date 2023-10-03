# input
n = int(input())

# top-down approach
d = [0] * (n+1)
def to1_td(n):
    if n == 1:
        return 0
    if d[n] != 0:
        return d[n]

    d[n] = to1_td(n-1) + 1
    if n%2 == 0:
        d[n] = min(d[n], to1_td(n//2)+1)
    if n%3 == 0:
        d[n] = min(d[n], to1_td(n//3)+1)
    if n%5 == 0:
        d[n] = min(d[n], to1_td(n//5)+1)
    return d[n]

print("top-down result: ", to1_td(n))

# bottom-up approach
def to1_bu(n):
    d = [0]*(n+1)
    
    for i in range(2,n+1):
        d[i] = d[i-1] + 1
        if i%2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i%3 == 0:
            d[i] = min(d[i], d[i//3]+1)
        if i%5 == 0:
            d[i] = min(d[i], d[i//5]+1)

    return d[n]

print("bottom-up result: ", to1_bu(n))
