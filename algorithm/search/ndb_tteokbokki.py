# 이코테 - 이진 탐색: 떡볶이 떡 만들기
n,m = list(map(int, input().split(' ')))
tteoks = list(map(int, input().split(' ')))

sp = 0
ep = max(tteoks)-1
i = 0

while sp<=ep:
    center = (sp+ep)//2
    sum_ = 0
    
    for t in tteoks:
        sum_ += max(t-center, 0)

    print(center, sum_, m)
    if sum_ == m:
        print(center)
        break
    elif sum_ > m:
        sp = center+1
    elif sum_ < m:
        ep = center-1
else:
    print(-1)

