# 이코테 2. 그리디 & 구현 - 곱하기 혹은 더하기

input_ = input()

result = int(input_[0])

for i in input_[1:]:
    if result <= 1 or int(i) <= 1:
        result += int(i)
    else:
        result *= int(i)

print(result)
