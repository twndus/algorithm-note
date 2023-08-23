seq = [9, 2, 5, 3, 1, 6, 7, 4, 8, 0]
print("before sorting: ", seq)

for i in range(len(seq)):
    min_val, min_idx = seq[i], i
    for j in range(i+1, len(seq)):
        if min_val > seq[j]:
            min_val, min_idx = seq[j], j
    seq[i], seq[min_idx] = seq[min_idx], seq[i]

print("after sorting:  ", seq)
