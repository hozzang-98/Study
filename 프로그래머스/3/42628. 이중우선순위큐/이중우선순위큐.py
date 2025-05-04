from heapq import heappush, heappop

def solution(operations):

    min_heap = []  # 최소 힙 (최솟값 관리)
    max_heap = []  # 최대 힙 (최댓값 관리)
    entry = {}  # 유효한 값만 관리하는 딕셔너리

    for operation in operations:
        action, value = operation.split()
        value = int(value)

        if action == "I":
            heappush(min_heap, value)  # 최소 힙에 삽입
            heappush(max_heap, -value)  # 최대 힙에 삽입 (음수로 변환하여 저장)
            entry[value] = entry.get(value, 0) + 1  # 삽입된 값 카운트 증가

        elif action == "D":
            if not entry:  # 큐가 비어 있으면 무시
                continue

            if value == 1:  # 최댓값 삭제
                while max_heap:
                    max_val = -heappop(max_heap)
                    if entry.get(max_val, 0) > 0:
                        entry[max_val] -= 1
                        if entry[max_val] == 0:
                            del entry[max_val]
                        break
            else:  # 최솟값 삭제
                while min_heap:
                    min_val = heappop(min_heap)
                    if entry.get(min_val, 0) > 0:
                        entry[min_val] -= 1
                        if entry[min_val] == 0:
                            del entry[min_val]
                        break

    if not entry:  # 모든 요소가 삭제되었으면 [0,0] 반환
    
        return [0, 0]

    # 최댓값과 최솟값 찾기
    while max_heap and entry.get(-max_heap[0], 0) == 0:
    
        heappop(max_heap)  # 유효하지 않은 값 제거
        
    while min_heap and entry.get(min_heap[0], 0) == 0:
    
        heappop(min_heap)  # 유효하지 않은 값 제거

    return [-max_heap[0], min_heap[0]]