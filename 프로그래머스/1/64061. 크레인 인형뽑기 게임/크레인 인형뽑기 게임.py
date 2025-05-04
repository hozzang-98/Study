def solution(board, moves):
    stack = []
    answer = 0

    for move in moves:
        for j in range(len(board)):
            if board[j][move - 1] != 0:
                doll = board[j][move - 1]
                board[j][move - 1] = 0  # 인형을 뽑았으니 해당 위치를 비우기
                
                if stack and stack[-1] == doll:  # 스택이 비어있지 않고, 같은 인형이면 터뜨리기
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)  # 바구니에 추가
                
                break  # 이미 인형을 뽑았으므로 더 이상 탐색할 필요 없음
                
    return answer