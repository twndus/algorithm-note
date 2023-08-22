# 프로그래머스: 단어 변환 https://school.programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque

def match(a, b):
    cnt = 0
    for ca,cb in zip(a,b):
        if ca != cb:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def solution(start, target, words):
    # 타겟이 없으면 0 반환
    if target not in words:
        return 0

    # 타겟을 변환해보자
    queue = deque([[0, start]])
    visited = [0] * len(words)

    while queue:
        step, v = queue.popleft()
        if v == target:
            return step
        for i, w in enumerate(words):
            if match(v, w) and not visited[i]:
                queue.append((step+1, w))
                visited[i] = 1

if __name__ == '__main__':
    start = "hit"
    target = "cog"
    words1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    ans1 = 4

    words2 = ["hot", "dot", "dog", "lot", "log"]
    ans2 = 0

    print(solution(start, target, words1), ans1)
    print(solution(start, target, words2), ans2)
