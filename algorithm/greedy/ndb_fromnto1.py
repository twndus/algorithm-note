# 이코테 2021 2. 그리디 & 구현 - N이 1이 될때까지

n, k = map(int, input().split(' '))

result = 0

## 비효율 코드
#while True:
#    if n%k:
#        n -= 1
#    else:
#        n //= k
#    result += 1
#    if n <= 1:
#        break

# 효율 코드
while True:
    target = (n//k)*k       # k로 나누어 떨어지는 가장 큰 n을 찾음
    result += n-target      # 나누어 떨어지는 k까지 -1하는 횟수
    n = target
    if n < k:               # k보다 작으면 나누지 않고 loop 탈출
        break
    n //= k
    result += 1

result += (n-1)             # 1보다 더 남았으면 -1 하는 만큼 더해줌
print(result)
