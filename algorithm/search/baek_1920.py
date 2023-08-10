# 문제: 수 찾기 https://www.acmicpc.net/problem/1920
from binary_search import binary_search

def solution():
    n = int(input())
    a_list = [int(i) for i in input().split(' ')]
    m = int(input())
    x_list = [int(i) for i in input().split(' ')]
    
    # sort
    a_list.sort()

    # O(nlogn)
    for x in x_list:
        if binary_search(a_list, x) == -1:
            print(0)
        else:
            print(1)

#    # O(n^2)
#    for x in x_list:
#        if x in a_list:
#            print(1)
#        else:
#            print(0)

if __name__ == '__main__':
    solution()
