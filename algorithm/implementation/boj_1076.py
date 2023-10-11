# BOJ 1076 저항
rmulti = {'black':1, 'brown': 1e1, 'red':1e2, 'orange':1e3, 'yellow':1e4,
    'green':1e5, 'blue':1e6, 'violet':1e7, 'grey':1e8, 'white':1e9}
rvalue = {'black':0, 'brown': 1, 'red':2, 'orange':3, 'yellow':4,
    'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}

answer = str(rvalue[input()]) + str(rvalue[input()]) + str(int(rmulti[input()]))[1:]
if int(answer) == 0:
    print(0)
else:
    print(int(answer))
