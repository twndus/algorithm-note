# BOJ 1789 수들의 합
s = int(input())
answer = 0
i = 1

while s > 0:
    s -= i
    i += 1
    answer += 1
    if s < i:
        s = 0

print(answer)
