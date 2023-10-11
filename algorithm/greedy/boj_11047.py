# problem: 동전 0 https://www.acmicpc.net/problem/11047

def main():
    n_k = input()
    n, k = int(n_k.split(' ')[0]), int(n_k.split(' ')[1])
    coins = []

    for i in range(n):
        coin = int(input())
        coins.append(coin)
    
    answer = 0

    for c in coins[::-1]:
        answer += k//c
        k %= c

        if k <= 0:
            break

    print(answer)

if __name__ == '__main__':
    main()
