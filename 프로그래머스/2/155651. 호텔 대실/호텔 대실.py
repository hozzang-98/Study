import heapq

def solution(book_time):
    # 예약 시간을 분 단위로 변환 후 정렬
    book_time = sorted([[int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:]) + 10] for s, e in book_time])
    
    heap = []  # 사용 중인 방의 종료 시간을 저장할 최소 힙

    for start, end in book_time:
        if heap and heap[0] <= start:
            heapq.heappop(heap)  # 기존 방을 재사용 가능하면 제거
        heapq.heappush(heap, end)  # 새 방의 종료 시간 추가

    return len(heap)  # 필요한 방의 개수