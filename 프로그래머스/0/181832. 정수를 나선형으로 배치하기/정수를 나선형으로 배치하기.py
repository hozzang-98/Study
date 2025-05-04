def solution(n):
    answer = [[0] * n for _ in range(n)]  # n x n 배열 초기화
    dx = [0, 1, 0, -1]  # 오른쪽, 아래, 왼쪽, 위 이동
    dy = [1, 0, -1, 0]
    
    x, y, direction = 0, 0, 0  # 시작 위치 (0,0) / 방향(오른쪽)
    
    for i in range(1, n * n + 1):
        answer[x][y] = i  # 현재 위치에 숫자 채우기
        nx, ny = x + dx[direction], y + dy[direction]  # 다음 위치 계산

        # 배열의 범위를 벗어나거나 이미 값이 채워진 경우 → 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            direction = (direction + 1) % 4  # 방향 변경 (오른쪽 → 아래 → 왼쪽 → 위 순환)
            nx, ny = x + dx[direction], y + dy[direction]

        x, y = nx, ny  # 위치 업데이트
    
    return answer