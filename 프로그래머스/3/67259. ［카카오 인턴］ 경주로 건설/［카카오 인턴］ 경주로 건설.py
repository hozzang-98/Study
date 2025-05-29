from collections import deque

def solution(board):
    N = len(board)
    directions = [(-1,0), (0,1), (1,0), (0,-1)]  # 상우하좌
    visited = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    q = deque()

    for d in [1, 2]:  # 오른쪽, 아래 시작
        visited[0][0][d] = 0
        q.append((0, 0, 0, d))  # x, y, cost, dir

    while q:
        x, y, cost, dir = q.popleft()
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                ncost = cost + (100 if i == dir else 600)
                if ncost < visited[nx][ny][i]:
                    visited[nx][ny][i] = ncost
                    q.append((nx, ny, ncost, i))

    return min(visited[N-1][N-1])