def solution(board):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    length = len(board)
    
    # 지뢰(1)가 있는 위치를 찾아 위험지역 표시
    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                for d in range(8):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                        board[nx][ny] = 2  # 위험 지역 표시

    # 안전한 지역(0) 개수 세기
    return sum(row.count(0) for row in board)