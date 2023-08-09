''' 
binary search

내림차순 또는 오름차순으로 정렬된 배열에서 보다 효율적으로
검색하는 방법
'''

def binary_search(array, elem):
    # sort
    array.sort()

    lower_bound = 0
    upper_bound = len(array)-1

    while lower_bound < upper_bound:
        index = (lower_bound+upper_bound)//2
        if array[index] == elem:
            return index 
        elif array[index] > elem:
            upper_bound = index
        elif array[index] < elem:
            lower_bound = index
    return -1


if __name__ == '__main__':
    array = []

    # input array size
    array_size = int(input("배열의 크기를 입력하세요: "))

    for i in range(array_size):
        array_elem = int(input(f"[{i}]번째 요소를 입력하세요: "))
        array.append(array_elem)

    elem = int(input("검색할 요소를 입력하세요: "))

    index = binary_search(array, elem)
    
    if index == -1:
        print(f"요소 {elem}가 배열{array} 에 없습니다.")
    else:
        print(f"요소 {elem}는 {index}에 있습니다.")

