# 프로그래머스: 여행경로 https://school.programmers.co.kr/learn/courses/30/lessons/43164
def solution(tickets):

    tickets = sorted(tickets, key=lambda x:x[1])
    path = ['ICN']
    queue = ['ICN']
    visited = [0]*len(tickets)
    for _ in tickets:
        start = path.popleft()
        for i, ticket in enumerate(tickets):
            if (ticket[0] == start) and (not visited[i]):
                start = ticket[1]
                visited[i] = 1
                path.append(ticket[1])
                queue.append(ticket[1])

    return path

if __name__ == '__main__':
    tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    return1 = ["ICN", "JFK", "HND", "IAD"]

    tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    return2 = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

    print(solution(tickets1), return1)
    print(solution(tickets2), return2)
