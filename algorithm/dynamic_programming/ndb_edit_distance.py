string_a = input()
string_b = input()

d = [0] * len(string_b)
i = 0

while i < len(string_b):
    if string_a[i] == string_b[i]:
        d[i] = d[i-1]
        i += 1
    elif string_a[i+1] == string_b[i]:
        d[i] = d[i-1]+1
        i += 2
    elif string_a[i-1] == string_b[i]:
        d[i] = d[i-1]+1
    else:
        d[i] = d[i-1]+1
        i += 1

print(d)
print(d[-1])
