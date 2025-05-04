def solution(board):

    answer = board[0][0]

    n = len(board)
    m = len(board[0])

    for i in range(1,n):

        for j in range(1,m):

            if board[i][j] == 1:

                # (i,j) 위치에서 좌상단, 상단, 좌측 모두 1 이상이어야 정사각형 확장 가능하며
                # 이 세 값 중 가장 작은 숫자에 1을 더한 것이 최대 정사각형 한 변의 길이
                board[i][j] = 1 + min(board[i-1][j-1], board[i-1][j], board[i][j-1])

                answer = max(answer, board[i][j])

    return answer ** 2