import time

# input
n = int(input())

# fibo with recursive function
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

start_time = time.time()
result = fibo(n)
runtime = time.time() - start_time
print("vanilla recursive function, result: ", result, "runtime: ", round(runtime, 4))

# fibo with top-down approach
d = [0]*(n+1)
def fibo_td(n):
    #print(f'f({n})', end=' ')
    if n==1 or n==2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo_td(n-1)+fibo_td(n-2) 
    return d[n]

start_time = time.time()
result = fibo_td(n)
runtime = time.time() - start_time
print("top-down approach, result: ", result, "runtime: ", round(runtime, 4))

# fibo with bottom-up approach
def fibo_bu(n):
    d = [0]*(n+1)
    d[1], d[2] = 1,1
    for i in range(3, n+1):
        d[i] = d[i-1]+d[i-2]
    return d[n]

start_time = time.time()
result = fibo_bu(n)
runtime = time.time() - start_time
print("bottom-up approach, result: ", result, "runtime: ", round(runtime, 4))
