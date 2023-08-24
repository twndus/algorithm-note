'''
Python의 내장 함수를 사용하자
'''

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print("bisect_left 의 결과:  ", bisect_left(a, x))
print("bisect_right 의 결과: ", bisect_right(a, x)) 

# a 배열에서 x의 개수
print(f"{a} 배열에서 {x}의 개수: ", bisect_right(a,x) - bisect_left(a,x))

# a 배열에서 [i, j] 범위에 포함되는 데이터의 개수
i = 2
j = 4
print(f"{a} 배열에서 [{i}, {j}] 범위 내 데이터의 개수: ",
    bisect_right(a,j) - bisect_left(a,i))
