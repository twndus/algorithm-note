a = input()
b = input()

if len(a) > len(b):
    a,b = b,a
#d = [0] * len(string_b)
#i = 0
#
#while i < len(string_b):
#    if string_a[i] == string_b[i]:
#        d[i] = d[i-1]
#        i += 1
#    elif string_a[i+1] == string_b[i]:
#        d[i] = d[i-1]+1
#        i += 2
#    elif string_a[i-1] == string_b[i]:
#        d[i] = d[i-1]+1
#    else:
#        d[i] = d[i-1]+1
#        i += 1
#
#print(d)
#print(d[-1])

d = [[0 for i in range(len(a))] for j in range(len(b))]

for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j]:
            d[i][j] = 1

#lcs = 0
#for l in range(len(a)):
#    if sum([d[i][l] for i in range(len(b))]) > 0:
#        lcs += 1
#lcs = 0
#c = len(a)-1
#print("len(b): ", len(b))
#for r in range(len(b)-1, 0, -1):
#    for i in range(c, -1, -1):
#        print(r,i,d[r][i])
#        if d[r][i] == 1:
#            c = i
#            lcs += 1
#            break
#print(lcs)

for l in d:
    print(l)

# not row first, but column first
for r in range(len(b)):
    for c in range(len(a)):
        if r == 0 and c == 0: continue
        if r == 0:
            d[r][c] = d[r][c]+d[r][c-1]
        elif c == 0:
            d[r][c] = d[r][c]+d[r-1][c]
        else:
            d[r][c] = d[r][c]+max(d[r][c-1], d[r-1][c])

#print(len(b)-lcs)
print(max([d[i][-1] for i in range(len(a))]))
