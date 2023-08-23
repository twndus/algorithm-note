seq = [9, 2, 5, 3, 1, 6, 7, 4, 8, 0]
print("before sorting: ", seq)

def q_sort(seq, start, end):

    if start<0 or start>=len(seq) or end>len(seq) or end<0: return
    pivot = seq[start]

    # 왼쪽부터 피봇보다 큰 수
    for j in range(start+1, end):
        if seq[j] > pivot:
            break
    else:
        j = -1 # 피봇보다 큰 수가 없으면 -1

    # 오른쪽부터 피봇보다 작은 수
    for k in range(end-1, start, -1):
        if seq[k] < pivot:
            break
    else:
        k = -1

    print(seq, start, end, f" j:{j}, k:{k}")
    if j==-1 and k==-1: return
    if j == -1:
        seq[k], seq[start] = seq[start], seq[k]
        q_sort(seq, k+1, end)
        q_sort(seq, start, k)
    elif k == -1:
        q_sort(seq, start+1, end)
    elif j < k:
        seq[j], seq[k] = seq[k], seq[j]
        q_sort(seq, start, end)
    elif j > k:
        seq[k], seq[start] = seq[start], seq[k]
        q_sort(seq, k+1, end)
        q_sort(seq, start, k)


q_sort(seq, 0, len(seq))

print("after sorting:  ", seq)
