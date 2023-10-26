# BOJ 1107 리모컨
n = int(input())
m = int(input())
brokens = []
if m > 0: brokens = list(map(int,input().split()))

now = 100

while now!=n: 
    now = n

# 5457
# 5457(3), 5456(5), 5458(4), 5455(6)

# 100
# 100=100 0

# 500000
# 500000(1) -> 499999(x) -> 38 27 15 -> 150000-50000

# 1
# 0+1 (2)


# 80000
# 80000 (x) -> 80001, 79999 ~ 77777

stack = [100]
dp = [0]*500001
while stack:
    number = stack.pop()
    if number+dp[number]-1 == n:
        break
    if number > 0 and not dp[number-1]:
        dp[number-1] = n-(number-1)
        stack.append(number-1)
    if not dp[number+1]:
        dp[number+1] = n-(number+1)
        stack.append(number+1)

print(dp[n])
