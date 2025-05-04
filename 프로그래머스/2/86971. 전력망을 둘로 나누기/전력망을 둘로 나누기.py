from collections import deque

def bfs(n, graph, start):

    visited = [False for i in range(n+1)]

    q = deque([start])
    visited[start] = True
    cnt = 0

    while q:

        node = q.popleft()
        cnt += 1

        for end in graph[node]:
            
            if visited[end] == False:

                q.append(end)
                visited[end] = True

    return cnt

def solution(n, wires):
    
    answer = n - 2

    for i in range(len(wires)):

        copy_wires = wires.copy()

        graph = [[] for i in range(n+1)] # 0번째는 팔요 X
        visited = [False for i in range(n+1)]

        copy_wires.pop(i) # i번째 전선 끊기

        # 끊은 상태에서 그래프 생성
        for wire in copy_wires:
            
            start, end = wire[0], wire[1]

            graph[start].append(end)
            graph[end].append(start)

        # START NODE 찾기
        for idx, end in enumerate(graph):

            if len(end) != 0: # 독립된 Node는 제외

                start = idx
                break

        cnts = bfs(n, graph, start)
        other_cnts = n - cnts
        
        if abs(cnts - other_cnts) < answer:

            answer = abs(cnts - other_cnts)
        

    return answer