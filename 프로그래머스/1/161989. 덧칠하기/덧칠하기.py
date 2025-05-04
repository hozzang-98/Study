def solution(n, m, section):
    answer = 0
    i = 0

    while i < len(section):
        # 현재 section[i]에서부터 m만큼 칠하고, 그 다음으로 넘어감
        start = section[i]
        end = start + m - 1
        answer += 1

        # 다음 시작점을 롤러 범위 바깥으로 이동
        while i < len(section) and section[i] <= end:
            i += 1

    return answer