# BOJ 1541 잃어버린 괄호
expr = input()
value = ''
op = 1 #-: 0 #+: 1
answer = 0

for c in expr:
    if op == 1 and (c == '+' or c == '-'):
        op = 1 if c=='+' else 0
        if value: answer += int(value)
        value = ''
    elif op == 0 and (c == '+' or c == '-'):
        if value: answer -= int(value)
        value = ''
    else:
        value += c
else:
    if op == 0:
        answer -= int(value)
    else:
        answer += int(value)

print(answer)



