def solution(m,n,board):

    board = [[i for i in _] for _ in board]

    point = 1

    while point != 0:

        li = []

        point = 0

        for i in range(m-1):

            for j in range(n-1):

                if board[i][j] ==  board[i][j+1] ==  board[i+1][j]==  board[i+1][j+1] != "-":

                    li.append([i,j])
                    point += 1
        
        for cut in li:

            x, y = cut[0], cut[1]
            board[x][y], board[x][y+1], board[x+1][y], board[x+1][y+1] = "-", "-", "-", "-"

        for k in range(m):

            for i in range(m-1):

                for j in range(n):

                    if board[i+1][j] == "-":

                        board[i+1][j] = board[i][j]
                        board[i][j] = "-"

    answer = 0

    for s in board:

        answer += s.count("-")

    return answer