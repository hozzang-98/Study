from collections import deque

def solution(bridge_length, weight, truck_weights):

    time = 0
    bridge = deque([0] * bridge_length)  # 다리 위 상태 (초기값은 0으로 채움)
    total_weight = 0  # 다리 위 트럭 총 무게
    truck_weights = deque(truck_weights)  # 대기 트럭을 deque로 변환

    while truck_weights or total_weight > 0:  # 대기 트럭이 있거나 다리 위에 트럭이 남아있다면 계속 진행
        time += 1
        total_weight -= bridge.popleft()  # 다리를 빠져나간 트럭 무게 제거

        if truck_weights and total_weight + truck_weights[0] <= weight:  # 새 트럭이 올라갈 수 있다면
            truck = truck_weights.popleft()
            bridge.append(truck)
            total_weight += truck
        else:  # 무게 초과로 트럭이 못 올라오면 0을 추가 (다리 길이 유지)
            bridge.append(0)

    return time
