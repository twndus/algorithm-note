# 백준 - 계단오르기 https://www.acmicpc.net/problem/2579
n = int(input())
stairs = [int(input()) for _ in range(n)]#[::-1]

#d = [0]*n
#d[0] = stairs[0]
#d[1] = stairs[0]+stairs[1]
#
#dn = [0]*n
#dn[0] = 1
#dn[1] = 2
#
#for i in range(2, n):
#
#    # 2개 전 값으로 세팅
#    d[i] = d[i-2]+stairs[i]
#
#    # 조건 2에 걸리지 않는 경우
#    if d[i] < d[i-1]+stairs[i] and dn[i-1] < 2:
#        d[i] = d[i-1]+stairs[i]
#        dn[i] = dn[i-1] + 1
#        print('1', i, dn[i-1], d[i-1], stairs[i], dn[i])
#        continue
#
#    # 조건 2에 걸리나, 지금 것을 안밟아도 값이 더 큰 경우
#    elif d[i] < d[i-1] and dn[i-1] >= 2:
#        d[i] = d[i-1]
#        dn[i] = 1
#        print('2', i, dn[i-1], d[i-1], stairs[i], dn[i])
#        continue
#
#    dn[i] = 1
#    print('3', i, dn[i-1], d[i-1], stairs[i], dn[i])
#
#print(max(d))

result = []

def recursive(pointer, score, continuous):
    print(pointer,score,continuous)
    if pointer >= n-1:
        if pointer == n-1 and continuous < 2:
            result.append(score)
        else:
            result.append(score)
    else:
        if continuous >= 2:
            if pointer < n-2: recursive(pointer+2, score+stairs[pointer+1], 1)
            #recursive(pointer+1, score, 1) # 연속적인 경우, 현재 칸을 건너뛰거나
#            recursive(pointer+2, score+stairs[pointer+1], 1) # 다음 칸을 짚어
        else:
            recursive(pointer+1, score+stairs[pointer], continuous+1)
            if pointer < n-2: recursive(pointer+2, score+stairs[pointer+1], 1)
#    print(pointer,score,continuous)
#    if pointer >= n:
#        result.append(score)
#    if pointer == n-1 and continuous < 2:
#        recursive(pointer+1, score+stairs[pointer], continuous+1)
#    else:
#        if continuous > 2:
#            recursive(pointer+2, score+stairs[pointer+1], 1)
#            recursive(pointer+1, score+stairs[pointer], continuous+1)
#        else:
#            recursive(pointer+1, score+stairs[pointer], continuous+1)
#            recursive(pointer+1, score, 1)

#    if pointer == n-1:
#        d.append(score)
#    else:
#        # 조건 2 미만의 연속 노드인 경우
#        if continuous < 2:
#            recursive(pointer+1, score+stairs[pointer], continuous+1)
#        else:
#            recursive(pointer+1, score, 1)

recursive(0, 0, 0)

print(result)
print(max(result))
