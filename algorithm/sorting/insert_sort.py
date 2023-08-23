seq = [9, 2, 5, 3, 1, 6, 7, 4, 8, 0]
print("before sorting: ", seq)

for i in range(1, len(seq)):
    for j in range(i, 0, -1):
        if seq[j] < seq[j-1]:
            seq[j], seq[j-1] = seq[j-1], seq[j]
        else:
            break


print("after sorting:  ", seq)
