# 백준 - 설탕 배달 https://www.acmicpc.net/problem/2839

n = int(input())

for i in range(n//5, -1, -1):
    if (n-i*5)%3 == 0:
        print(i+(n-i*5)//3)
        exit()
else:
    print(-1)
