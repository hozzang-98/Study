from collections import deque

def solution(maps):

    n, m = len(maps), len(maps[0])
    directions = [(1,0), (0,1), (-1,0), (0,-1)]  # 동, 남, 서, 북
    queue = deque([(0, 0, 1)])  # (x, y, 이동거리)
    
    while queue:
    
        x, y, dist = queue.popleft()
        
        if (x, y) == (n-1, m-1):  # 목표 지점 도달 시 즉시 반환
        
            return dist

        for dx, dy in directions:
        
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
            
                queue.append((nx, ny, dist + 1))
                maps[nx][ny] = 0  # 방문 처리 (더 빠른 실행)
    
    return -1  # 도달 불가능