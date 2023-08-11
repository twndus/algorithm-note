# 이코테 2. 그리디 & 구현 - 모험가 길드

adventurers = list(map(int, input().split(' ')))

## 잘못 푼 방법: 모든 모험가를 보내지는 않아도 된다는 제약 조건에 따라 내림차순이 아닌 오름차순 접근 필요
## 내림차순 정렬
#adventurers.sort(reverse=True)
#
#result = 0
#size = adventurers[0]
#grouped = 1
#
#for p in adventurers[1:]:
#    if size > grouped:
#        grouped += 1
#    elif size == grouped:
#        grouped = 1
#        size = p
#        result += 1
#    print(size, grouped, result)
#
#if size == grouped:
#    result += 1

# 오름차순 정렬
adventurers.sort()

result = 0
size = adventurers[0]
grouped = 1

for p in adventurers[1:]:
    if size <= grouped:
        result += 1
        size = p
        grouped = 1
    else:
        grouped += 1
    print(result, size, grouped)

print(result)
