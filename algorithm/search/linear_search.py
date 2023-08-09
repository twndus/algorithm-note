# linear search

def linear_search(array, elem):
    for i, e in enumerate(array):
        if elem == e:
            return i
    return -1

if __name__ == '__main__':
    array = []

    # input array size
    array_size = int(input("배열의 크기를 입력하세요: "))

    for i in range(array_size):
        array_elem = input(f"[{i}]번째 요소를 입력하세요: ")
        array.append(array_elem)

    elem = input("검색할 요소를 입력하세요: ")

    index = linear_search(array, elem)
    
    if index == -1:
        print(f"요소 {elem}가 배열{array_elem} 에 없습니다.")
    else:
        print(f"요소 {elem}는 {index}에 있습니다.")

