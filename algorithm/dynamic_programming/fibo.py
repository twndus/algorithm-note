# DP 탑다운 예시: 피보나치 수열

n = int(input())
d = [-1] * (n+1)

d[1] = 1
d[2] = 1

# simple way
def _fibo(n):
    if n==1 or n==2:
        return 1
    else:
        result = fibo(n-1) + fibo(n-2)
        return result

# top-down
def fibo(n):
    if d[n]!= -1:
        return d[n]
    else:
        d[n] = fibo(n-1) + fibo(n-2)
        return d[n]

# bottom-up
def _fibo(n):
    d = [-1] * (n+1)
    d[1] = 1
    d[2] = 1

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
    
    return d[n]

print(fibo(n))
