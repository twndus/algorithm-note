from collections import Counter

seq = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
print("before sorting: ", seq)

cnt = Counter(seq)
new_seq = []

for k in sorted(cnt.keys()):
    new_seq.extend([k]*cnt[k])

print("after sorting: ", new_seq)
