import heapq

def min_heap(iterable):
    h = []
    newh = []

    for value in iterable:
        heapq.heappush(h, value)

    for _ in iterable:
        newh.append(heapq.heappop(h))    
    
    return newh

ex1 = [3, 0, 8, 4, 2, 6, 1, 7, 5, 9]
print(min_heap(ex1))

