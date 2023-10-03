# input
n = int(input())

d = [2, 3, 4, 5] #1
i = 6

while len(d)<n:
    is_ugly = False
     
    for e in d[::-1]:
        if i%e == 0 and i//e in {2,3,5}:
            is_ugly = True
            break

    if is_ugly:
        d.append(i)
    
    i += 1

d = [1]+d

print(d[n-1])
