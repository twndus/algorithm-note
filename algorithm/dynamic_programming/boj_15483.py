# 백준 - 최소 편집 https://www.acmicpc.net/problem/15483
a = input()
b = input()

dp_len = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
dp_track = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)] # same:1, x: 2, y: 3

# alignment
for ai in range(1,len(a)+1):
    for bi in range(1, len(b)+1):
        if a[ai-1] == b[bi-1]:
            dp_len[ai][bi] = dp_len[ai-1][bi-1] + 1
            dp_track[ai][bi] = 1
        elif dp_len[ai-1][bi] < dp_len[ai][bi-1]:
            dp_len[ai][bi] = dp_len[ai][bi-1]
            dp_track[ai][bi] = 2
        else:
            dp_len[ai][bi] = dp_len[ai-1][bi]
            dp_track[ai][bi] = 3

# check lcs
ai,bi = len(a), len(b)
result = 0#'' #0
before = 0

while ai > 0 and bi > 0:
#    if dp_len[ai][bi] == 0:
#        result += bi
#        break
    print(ai, bi, result)
    if dp_track[ai][bi] == 1:
        #result += a[ai-1]
        before, dp_track[ai][bi] = 1, -1
        #dp_track[ai][bi] = -1
        ai, bi = ai-1, bi-1
    elif dp_track[ai][bi] == 2:
        if before != 3: result += 1
        before = 2
        ai, bi = ai, bi-1
    else:
        if before != 2: result += 1
        before = 3
        ai, bi = ai-1, bi
#else:
#    if ai <= 0:
#        result += bi
#    else:
#        result += ai

for row in dp_track:
    print(row)

print(result)#[::-1])

