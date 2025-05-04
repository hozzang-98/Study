def solution(distance, rocks, n):
    rocks.append(distance)  # 도착지점을 rocks에 추가
    rocks.sort()  # 정렬

    left, right = 1, distance  # 최소 거리 범위 설정

    while left <= right:
        mid = (left + right) // 2  # 거리의 최솟값 후보
        current, removed = 0, 0  # 현재 위치, 제거한 바위 개수

        for rock in rocks:
            if rock - current < mid:  # mid보다 짧은 거리는 제거
                removed += 1
            else:
                current = rock  # 바위 유지

        if removed > n:  # 너무 많이 제거했다면 mid 줄이기
            right = mid - 1
        else:  # n개 이하로 제거했으면 mid 늘리기
            left = mid + 1  # 최소 거리를 늘려본다

    return right  # 최적의 최소 거리 반환