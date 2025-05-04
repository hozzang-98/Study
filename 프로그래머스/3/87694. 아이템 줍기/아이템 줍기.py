
def solution(rectangle, characterX, characterY, itemX, itemY):

    from collections import deque

    answer = 0
    field = [[-1]*102 for i in range(102)] # 겹치는 부분을 방지하기 위헤 2배 처리

    for r in rectangle:

        x1, y1, x2, y2 = map(lambda x: x*2, r)

        for x in range(x1, x2+1):
            
            for y in range(y1, y2+1):

                if x1 < x < x2 and y1 < y < y2: # 사각형 내부 

                    field[x][y] = 0 # 지나갈 수 없음

                elif field[x][y] != 0: # 이전 사각형의 내부가 아니면서 테두리인 곳

                    field[x][y] = 1 # 지나갈 수 있음

    visited = [[1]*102 for i in range(102)] 

    dx = [1,0,0,-1]
    dy = [0,1,-1,0]

    q = deque()

    q.append([characterX*2,characterY*2])

    while q:

        x, y = q.popleft() # BFS
        
        if (x == itemX * 2) and (y == itemY * 2):

            answer = visited[x][y] // 2

            break

        for d in range(4):
            
            next_x = x + dx[d]
            next_y = y + dy[d]

            if field[next_x][next_y] == 1 and visited[next_x][next_y] == 1: # (갈 수 있는 곳) & (아직 안 간 곳)

                q.append([next_x, next_y])
                visited[next_x][next_y] = visited[x][y] + 1

    return answer