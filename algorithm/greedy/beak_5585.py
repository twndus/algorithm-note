# 거스름돈 문제: https://www.acmicpc.net/problem/5585

def greedy_charge()
    coins = [500, 100, 50, 10, 5, 1]
    price = 1000-int(input())
    num_coins = 0

    for c in coins:
        num_coins += price//c
        price %= c
        
        if price <= 0:
            break

    print(num_coins)
    return num_coins


if __name__ == '__main__':
    greedy_charge()
