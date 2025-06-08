def solution(cap, n, deliveries, pickups):
    answer = 0
    d_idx = n - 1  # 가장 마지막 배달할 집 인덱스
    p_idx = n - 1  # 가장 마지막 수거할 집 인덱스

    while d_idx >= 0 or p_idx >= 0:
        # 배달/수거할 남은 위치 찾기
        while d_idx >= 0 and deliveries[d_idx] == 0:
            d_idx -= 1
        while p_idx >= 0 and pickups[p_idx] == 0:
            p_idx -= 1

        # 더 이상 남은 게 없으면 종료
        if d_idx < 0 and p_idx < 0:
            break

        # 현재 트럭이 갈 수 있는 가장 먼 거리
        distance = max(d_idx, p_idx) + 1
        answer += distance * 2

        # 배달, 수거 처리
        delivery_load = cap
        pickup_load = cap

        # 먼 집부터 배달 처리
        while d_idx >= 0 and delivery_load > 0:
            if deliveries[d_idx] <= delivery_load:
                delivery_load -= deliveries[d_idx]
                deliveries[d_idx] = 0
                d_idx -= 1
            else:
                deliveries[d_idx] -= delivery_load
                delivery_load = 0

        # 먼 집부터 수거 처리
        while p_idx >= 0 and pickup_load > 0:
            if pickups[p_idx] <= pickup_load:
                pickup_load -= pickups[p_idx]
                pickups[p_idx] = 0
                p_idx -= 1
            else:
                pickups[p_idx] -= pickup_load
                pickup_load = 0

    return answer