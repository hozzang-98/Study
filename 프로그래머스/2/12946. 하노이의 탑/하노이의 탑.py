def hanoi(n, start, end, help):

    if n == 1:
        return [[start, end]]  # 원판이 하나면 바로 이동

    moves = []  # 이동 경로를 저장할 리스트

    # 1. n-1개의 원판을 보조 기둥으로 이동 (end를 보조 기둥으로 활용)
    moves.extend(hanoi(n - 1, start, help, end))

    # 2. 가장 큰 원판을 목표 기둥으로 이동
    moves.append([start, end])

    # 3. n-1개의 원판을 목표 기둥으로 이동 (start를 보조 기둥으로 활용)
    moves.extend(hanoi(n - 1, help, end, start))

    return moves  # 최종 이동 리스트 반환

def solution(n):

    return hanoi(n, 1, 3, 2)