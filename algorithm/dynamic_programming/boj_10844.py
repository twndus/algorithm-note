# input
n = int(input())
result = 0

def recursive(i):
    global result
    if len(str(i)) >= n:
        for ci in range(1,len(str(i))):
            if str(i)[ci]+1 != str(i)[ci-1] and str(i)[ci]-1 != str(i)[ci-1]:
                break
        else:
            result += 1
    else:
        for j in range(10):
            recursive(str(i)+str(j))

recursive(n)
print(result)
