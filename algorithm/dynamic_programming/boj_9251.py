# 백준 - LCS https://www.acmicpc.net/problem/9251
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

print(dp_len[-1][-1])
