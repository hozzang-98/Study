from collections import deque

def bfs(x, y, board, visited, state):
    """BFS로 퍼즐 조각을 탐색하여 좌표 리스트 반환"""
    n = len(board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque([(x, y)])
    puzzle = []
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        puzzle.append((x, y))

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == state:
                visited[nx][ny] = 1
                q.append((nx, ny))

    return puzzle

def search_puzzle(board, state):
    """보드에서 특정 상태(0 or 1)의 퍼즐 조각을 찾아 리스트로 반환"""
    n = len(board)
    visited = [[0] * n for _ in range(n)]
    blocks = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == state and not visited[i][j]:  # 빈칸(0) 또는 블록(1) 탐색
                blocks.append(bfs(i, j, board, visited, state))

    return blocks

def extract_puzzle(puzzle):
    """퍼즐 조각을 2D 배열로 변환"""
    x_coords, y_coords = zip(*puzzle)
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    r, c = max_x - min_x + 1, max_y - min_y + 1
    puzzle_array = [[0] * c for _ in range(r)]

    for x, y in puzzle:
        puzzle_array[x - min_x][y - min_y] = 1

    return puzzle_array

def rotate_90(matrix):
    """2D 리스트를 90도 시계방향 회전"""
    return [[matrix[j][i] for j in range(len(matrix) - 1, -1, -1)] for i in range(len(matrix[0]))]

def get_all_rotations(puzzle):
    """퍼즐의 4가지 회전 상태를 반환"""
    rotations = []
    current = puzzle
    for _ in range(4):
        current = rotate_90(current)
        rotations.append(current)
    return rotations

def solution(game_board, table):
    """게임 보드의 빈칸을 테이블의 블록으로 채우는 최적의 조합을 찾는 함수"""
    game_blocks = [extract_puzzle(block) for block in search_puzzle(game_board, 0)]
    table_blocks = [extract_puzzle(block) for block in search_puzzle(table, 1)]
    
    answer = 0
    used = set()

    for empty in game_blocks:
        for i, table_block in enumerate(table_blocks):
            if i in used:  # 이미 사용한 블록이면 건너뛰기
                continue

            rotated_blocks = get_all_rotations(table_block)
            if any(rotated_block == empty for rotated_block in rotated_blocks):
                answer += sum(sum(row) for row in empty)
                used.add(i)  # 사용한 블록을 기록
                break

    return answer