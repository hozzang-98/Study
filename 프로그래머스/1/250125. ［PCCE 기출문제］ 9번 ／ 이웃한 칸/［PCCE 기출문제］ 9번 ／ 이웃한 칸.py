def solution(board, h, w):

    answer = 0
    n = len(board)

    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    
    for i in range(4):

        h_check = h + dx[i]
        w_check = w + dy[i]

        if (0 <= h_check < n) and 0 <= w_check < n:

            if board[h][w] == board[h_check][w_check]:

                answer += 1

    return answer