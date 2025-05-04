def solution(n, computers):
    answer = 0
    def dfs(i):
        visited[i] = 1 # 들른 처리
        for k in range(n):
            if computers[i][k]==1 and visited[k]==0:
                dfs(k)

    visited = [0 for i in range(n)]
    for i in range(n):
        if visited[i] == 0: # 안들렀으면
            dfs(i)
            answer += 1
    print('1')
    return answer