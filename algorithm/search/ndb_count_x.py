# 이코테 - 이진탐색: 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_right, bisect_left

n,x = list(map(int, input().split(' ')))
nums = list(map(int, list(input())))

print(bisect_right(nums,x)-bisect_left(nums,x))

