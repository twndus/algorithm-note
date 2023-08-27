def solution(n, m, maps):
    for im in range(1, m):
        for in_ in range(n):
            options = [maps[in_][im-1]]
            if in_ > 1:
                options.append(maps[in_-1][im-1])
            if in_ < n-1:
                options.append(maps[in_+1][im-1])
            maps[in_][im] = maps[in_][im] + max(options)
            #print(in_, im, maps[in_][im])
    return max([row[-1] for row in maps])

if __name__ == '__main__':
    test_nums = int(input())

    test_data = [] 
    for i in range(test_nums):
        n, m = list(map(int, input().split()))
        maps = list(map(int, input().split()))
        maps = [maps[i*m:(i+1)*m] for i in range(n)]
        test_data.append((n,m,maps))

    for td in test_data:
        print(solution(td[0], td[1], td[2]))


