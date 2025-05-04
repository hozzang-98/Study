def solution(name):

    answer = 0
    min_move = len(name) - 1  # 오른쪽으로만 이동하는 경우

    for i, char in enumerate(name):
        # ▲, ▼ 최소 이동
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 연속된 'A' 확인
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        # 최소 커서 이동 계산
        min_move = min(min_move, i + i + len(name) - next_idx, i + 2 * (len(name) - next_idx))

    return answer + min_move