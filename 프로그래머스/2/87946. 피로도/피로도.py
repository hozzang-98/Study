def solution(k, dungeons):

    max_cnt = 0
    visited = [False] * len(dungeons)  # 방문 여부 체크
    
    def dfs(k, count):
    
        nonlocal max_cnt
        max_cnt = max(max_cnt, count)  # 최대 던전 개수 갱신

        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:  # 방문 안 했고 탐험 가능하면 진행
                visited[i] = True
                dfs(k - dungeons[i][1], count + 1)  # 피로도 차감 후 탐험
                visited[i] = False  # 백트래킹 (다른 경로 탐색을 위해 원상 복구)

    dfs(k, 0)  # 초기 탐색 시작
    
    return max_cnt