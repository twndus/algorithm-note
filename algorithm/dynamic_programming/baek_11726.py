# 백준: 2xn 타일링 https://www.acmicpc.net/problem/11726
from math import factorial

n = int(input())
answer = 0
d_fact = [-1 for _ in range(n+1)]

def get_fact(n):
    if d_fact[n] != -1:
        return d_fact[n]
    else:
        return factorial(n)

for i in range(n//2+1):
    answer += get_fact(i+n-(i*2))//get_fact(i)//get_fact(n-(i*2))

print(int(answer)%10007)


